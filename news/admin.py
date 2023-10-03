from django.contrib import admin, messages
from .models import Articles, Category
from django.utils.translation import ngettext


class CategoryAdmin(admin.ModelAdmin):

    def make_published(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(
            request,
            ngettext(
                "%d دسته‌بندی با موفقیت فعال شد.",
                "%d دسته‌بندی با موفقیت فعال شد.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    make_published.short_description='فعالسازی دسته‌بندی‌های انتخاب شده'

    def make_draft(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(
            request,
            ngettext(
                "%d دسته‌بندی با موفقیت غیرفعال شد.",
                "%d دسته‌بندی با موفقیت غیرفعال شد.",
                updated,
            )
            % updated,
            messages.SUCCESS,
        )
    make_draft.short_description='غیرفعال کردن دسته‌بندی‌های انتخاب شده'

    list_display = ('title', 'position', 'parent', 'slug', 'status')
    list_filter = (['status'])
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'slug')
    actions=[make_published, make_draft]
    ordering=['-status', 'parent__id', 'title']

admin.site.register(Category, CategoryAdmin)

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

    list_display = ('title','picture', 'writer', 'category_to_str', 'jcreated', 'jpublished', 'status')
    list_filter = ('status', 'published')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description')
    ordering=['-status', '-published']
    actions=[make_published, make_draft]

admin.site.register(Articles, ArticleAdmin)
