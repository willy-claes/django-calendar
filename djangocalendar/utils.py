import calendar
import datetime as dt
from django.apps import apps
from djangocalendar.settings import conf

def get_calendar_data(adate, model_str=None, lookup=None,
                      title=None, slug=None):
    first, last = calendar.monthrange(adate.year, adate.month)
    lf = lookup if lookup else conf['LF']
    tf = title if title else conf['TF']
    sf = slug if slug else conf['SF']
    dkeys = (lf + '__gte', lf + '__lte')
    qd = dict(zip(dkeys, (dt.date(adate.year, adate.month, 1),
                          dt.date(adate.year, adate.month, last))))

    model_str = model_str if model_str else conf['MODEL']
    model = apps.get_model(*model_str.split('.'))
    dates = model.objects.filter(**qd).datetimes(lf, 'day')

    nums = [i.day for i in dates]
    one_day_range = lambda x: dict(zip(dkeys, (x, x + dt.timedelta(days=1))))
    objs = model.objects.only(tf, sf) if tf and sf else model.objects.all()
    dobj = [objs.filter(**one_day_range(i)) for i in dates]
    days = list(range(1, last+1))

    f = lambda x: (x, None) if x not in nums else (x, dobj[nums.index(x)])
    mdays = [[conf['FILL'] if i < first else f(days.pop(0)) for i in range(7)]]
    for i in range(5):
        w = []
        for j in range(7):
                w.append(f(days.pop(0)) if len(days) > 0 else conf['FILL'])
        mdays.append(w)

    weekdays = (dt.date(2001, 1, i+1) for i in range(7))
    return {
        'weekdays': weekdays, 'mdays': mdays,
        'cachetime': conf['CACHE'], 'month': adate,
        'model': model_str, 'lookup': lf,
        'tf': tf, 'sf': sf,
    }
