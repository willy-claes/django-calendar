from django.conf.urls import url
from djangocalendar import views

urlpatterns = [
    url(r'^get_table/$', views.get_calendar_table, name='table'),
]
