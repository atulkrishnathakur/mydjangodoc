from django import template

register = template.Library()


@register.simple_tag
def akt(a):
    return a + 1
    
counter = 0
@register.simple_tag
def counter_tag():
    global counter
    counter += 1
    return counter

@register.simple_tag
def rowcss(status):
    if status == 1:
        return 'active'
    else:
        return 'inactive'