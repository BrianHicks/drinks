'percent format'
from django import template

register = template.Library()


@register.filter(is_safe=True)
def percentage(num):
    return num
    #return '%.2f%%' % (num * 100) # broken for now
