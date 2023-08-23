from django import template

register = template.Library()


@register.filter(name='count_by_state')
def count_by_state(queryset, states):
    states=states.split(',')
    return queryset.filter(state__in=states).count()

