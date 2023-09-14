from django import template
from ..models import Category

register = template.Library()


@register.simple_tag
def title(defualt='دیجی آنلاین'):
    return defualt


@register.inclusion_tag('news/inclusion_tags/navbar.html')
def navbar():
    return {'Categories': Category.objects.filter(status=True)}
