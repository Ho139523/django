from django.db import models
from django.urls import reverse
from accounts.models import User
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html


# My managers

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

    def active(self):
        return self.filter(status=True)

# My models
class Category(models.Model):
    parent=models.ForeignKey("self", null=True, default=None, blank=True, related_name='subcat', on_delete=models.SET_NULL, verbose_name='زیردسته')
    title=models.CharField(max_length=100, verbose_name='عنوان دسته‌بندی')
    slug=models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته‌بندی')
    status=models.BooleanField(default=True, verbose_name='آیا نشان داده شود؟')
    position=models.IntegerField(verbose_name='اهمیت')

    class Meta:
        verbose_name='دسته‌بندی'
        verbose_name_plural='دسته‌بندی‌ها'
        ordering=['parent__id', 'position', 'status']

    def __str__(self):
        return self.title

    objects=ArticleManager()


class Articles(models.Model):
    options=(('d', "پیش‌نویس"), ('p', "منتشر شده"))
    title = models.CharField(max_length=200, verbose_name='عنوان')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='articles', verbose_name='نویسنده')
    category=models.ManyToManyField(Category, verbose_name='دسته‌بندی', related_name='articles')
    description = models.TextField(max_length=1000000, verbose_name='جزییات خبر')
    slug=models.SlugField(max_length=100, unique=True, verbose_name='آدرس')
    image=models.ImageField(upload_to='images', verbose_name='تصویر خبر')
    published=models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    created=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ تولید')
    Updated=models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')
    status=models.CharField(max_length=1, choices=options, verbose_name='وضعییت')

    class Meta:
        verbose_name='خبر'
        verbose_name_plural='اخبار'
        ordering=['-published']
    def __str__(self):
        return self.title

    def jpublished(self):
        return jalali_converter(self.published)

    jpublished.short_description='تاریخ انتشار'

    def get_absolute_url(self):
        return reverse('accounts:profile')

    def jcreated(self):
        return jalali_converter(self.created)

    jcreated.short_description='تاریخ تولید'


    objects=ArticleManager()

    def picture(self):
        return format_html("<img src='{}' width=100px style='border-radius: 10px;'>".format(self.image.url))

    picture.short_description='عکس'

    def category_to_str(self):
        return "، ".join([category.title for category in self.category.active()])
    category_to_str.short_description='دسته‌بندی'
