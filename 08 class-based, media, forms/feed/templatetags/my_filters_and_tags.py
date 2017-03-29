from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def truncate(value):
    res = value[:10] + "..." if len(value) > 10 else value
    return res

@register.filter()
def render(image):
    if image:
        return "<img src='%s'/>" % (image.url)
    else:
        return ""

@register.simple_tag()
def who(items):
    return ", ".join(set([t.user.username for t in items]))
