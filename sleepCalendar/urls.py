from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'sleepCalendar'
urlpatterns = [
	url('^$', views.indexView, name='index'),
	url('^calendar$', views.CalendarDetails.as_view()),
	url('calendar/uuid/(?P<uuid>[-\w]+)$', views.CalendarDetails.as_view()),
	url('calendar/year/(?P<date__year>\d+)$', views.CalendarListWithYear.as_view()),
	url('calendar/year/(?P<date__year>\d+)/month/(?P<date__month>\d+)$', views.CalendarListWithYearAndMonth.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
