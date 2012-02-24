'percent format'
from django import template

register = template.Library()


@register.filter
def percentage(num):
    return '{0:.2%}'.format(num)
