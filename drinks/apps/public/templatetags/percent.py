'percent format'
from django import template

register = template.Library()


@register.filter
def percentage(num):
    return num
    #return '%.2f%%' % (num * 100) # broken for now
