import datetime as dt
from django import template

from djangocalendar.utils import get_calendar_data
register = template.Library()

@register.inclusion_tag('base_calendar.html')
def get_calendar(m=None, lf=None, tf=None, sf=None, adate=None):
    today = adate if adate else dt.date.today()
    return get_calendar_data(today, m, lf, tf, sf)
