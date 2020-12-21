from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^journal/add/(?P<pk>[0-9]+)/$', views.JournalCreate.as_view(), name='journal-add'),
    url(r'^journal/update/(?P<pk>[0-9]+)/$', views.JournalUpdate.as_view(), name='journal-update'),
    url(r'^journal/delete/(?P<pk>[0-9]+)/$', views.JournalDelete.as_view(), name='journal-delete'),
]
