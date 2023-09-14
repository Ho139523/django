from django.contrib import admin, messages
from .models import Articles, Category
from django.utils.translation import ngettext


class AdminCategory(admin.ModelAdmin):
    list_display = ('title', 'position', 'parent', 'slug', 'status')
    list_filter = (['status'])
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'slug')

admin.site.register(Category, AdminCategory)

class ArticleAdmin(admin.ModelAdmin):

    def make_published(self, request, queryset):
        updated = queryset.update(status="p")
        self.message_user(
            request,
            ngettext(
                "%d مقاله با موفقیت منتشر شد.",
                "%d مقاله با موفقیت منتشر شد.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    make_published.short_description='انتشار مقالات انتخاب شده'

    def make_draft(self, request, queryset):
        updated = queryset.update(status="d")
        self.message_user(
            request,
            ngettext(
                "%d مقاله با موفقیت پیش‌نویس شد.",
                "%d مقاله با موفقیت پیش‌نویس شد.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    make_draft.short_description='پیش‌نویس کردن مقالات انتخاب شده'

    list_display = ('title','picture', 'category_to_str', 'jcreated', 'jpublished', 'status')
    list_filter = ('status', 'published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    ordering=['-status', '-published']
    actions=[make_published, make_draft]


    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.published_category()])
    category_to_str.short_description='دسته‌بندی'
admin.site.register(Articles, ArticleAdmin)
