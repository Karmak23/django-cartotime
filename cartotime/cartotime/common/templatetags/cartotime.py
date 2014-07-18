from django import template

register = template.Library()

@register.filter
def by_start_date(things):
    return things.all().order_by('start_date')
