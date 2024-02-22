from django import template

register = template.Library()


@register.filter(name="getattribute")
def getattribute(value, arg):
    return getattr(value, arg)
