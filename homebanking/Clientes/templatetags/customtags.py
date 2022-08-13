from django import template

register = template.Library()

def decim(value):
    value = str(value)
    i = len(value) - 2
    value = value[:i] + ',' + value[i:]
    return value

register.filter('decim', decim)

def hidenum(value):
    value = str(value)
    i = len(value) - 4
    value = value[i:]
    return value

register.filter('hidenum', hidenum)