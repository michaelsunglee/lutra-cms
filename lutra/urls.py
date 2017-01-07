from django.conf.urls import url
from django.contrib import admin
from notescms import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.NotesView.as_view(), name='index'),
]
