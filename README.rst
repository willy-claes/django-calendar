===============
Django-calendar
===============

Django-calendar is a Django application that gives you a simple calendar, based on your custom model, which you can use directly in the template.

Quick start
-----------

1. Add "djangocalendar" to your INSTALLED_APPS::

    INSTALLED_APPS = [
        ...
        'djangocalendar',
    ]

2. Set up the configuration of the calendar if you wish::

    DJANGOCALENDAR_CONFIG = {
        'FILL': '-',  # filler of the empty cell
        'MODEL': 'catalog.Article',  # model used by calendar
        'LF': 'add_date',  # lookup field
        'TF': 'title',  # title field
        'SF': 'slug',  # slug field
        'CACHE': 0 # cache time in seconds
    }

3. Include the djangocalendar URLconf in your project urls.py like this::

    url(r'^djangocalendar/', include('djangocalendar.urls', namespace='djangocalendar')),

4. Add calendar extras to you template::

    {% load djangocalendar_extras %}

5. Place calendar somewhere in the template:

    5.1. If you defined calendar configuration in project settings::

        {% get_calendar %}

    5.2. If you want to set up configuration directly in the template::

        {% get_calendar 'catalog.Article' 'add_date' 'title' 'slug' adate=date %}

    5.3. If you want define an exact date::

        {% get_calendar adate=date %}

6. For the switching months you can use navigation buttons.
