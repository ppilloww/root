from django import template
register = template.Library()

@register.filter
def duration(value):
    if value is None:
        return None
    total_seconds = int(value.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return '{}:{:02}'.format(hours, minutes)