from django import template

from visitstat import models

register = template.Library()


@register.simple_tag
def visitstat_views_today():
    return models.Visit.get_views_today()


@register.simple_tag
def visitstat_visitors_24():
    return models.Visit.get_visitors_24()


@register.simple_tag
def visitstat_visitors_today():
    return models.Visit.get_visitors_today()
