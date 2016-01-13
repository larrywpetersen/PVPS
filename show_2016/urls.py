from django.conf.urls import url

from . import views


urlpatterns = [
    url( r'^$', views.index, name='index'),
    url( r'^index$', views.index, name='index'),

    url( r'^entry_form$', views.entry_form, name='entry_form'),
    url( r'^entry_action$', views.entry_action, name='entry_action'),

    url( r'^list_entries$', views.list_entries, name='list_entries'),

#    url( r'^list_pics$', views.list_pics, name='list_pics'),

    url( r'^list_pics/(?P<sortkey>[^/]*)$', views.list_pics, name='list_pics'),

    url( r'^detail/(?P<entryid>[0-9]*)$', views.detail, name='detial'),

    url( r'^wallcards$', views.print_wallcards, name='wallcards'),

]

