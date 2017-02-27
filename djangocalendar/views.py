import datetime as dt
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page
from djangocalendar.utils import get_calendar_data
from djangocalendar.settings import conf

@cache_page(conf['CACHE'])
def get_calendar_table(request):

    if request.is_ajax() and 'sign' in request.GET and 'date' in request.GET:
        old_date = dt.datetime.strptime(request.GET['date'], '%Y%m%d').date()
        if old_date.month == 1 and request.GET['sign'] == '-1':
            cm, cy = 12, -1
        elif old_date.month == 12 and request.GET['sign'] == '1':
            cm, cy = -12, 1
        else:
            cm, cy = 0, 0
        model = request.GET.get('model')
        lookup = request.GET.get('lookup')
        title = request.GET.get('title')
        slug = request.GET.get('slug')
        new_date = dt.date(old_date.year + cy,
                           old_date.month + int(request.GET['sign']) + cm, 1)
        data = get_calendar_data(new_date, model, lookup, title, slug)
        return render_to_response('table.html', data)
