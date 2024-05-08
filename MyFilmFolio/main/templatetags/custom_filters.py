from django import template

register = template.Library()

@register.filter(name='truncate_words')
def truncate_words(value, arg):
    words = value.split()
    if len(words) > arg:
        return ' '.join(words[:arg]) + ' ...'
    else:
        return value
