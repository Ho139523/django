from django.http import Http404
class SuperseesMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields=['title', 'writer', 'category', 'description', 'slug', 'image', 'published', 'status']
        elif request.user.is_author:
            self.fields=['title', 'category', 'description', 'slug', 'image', 'published']
        else:
            raise Http404("این صفحه فقط برای نویسندگان قابل نمایش است.")
        return super().dispatch(request, *args, **kwargs)
