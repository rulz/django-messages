from django import template

register = template.Library()


@register.filter('split')
def split(value, arg):
    print value.split(arg)
    return value.split(arg)[7]