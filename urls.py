from django.conf.urls import url
from . import views

app_name = 'pastebin'
urlpatterns=[
    url(r'^$', views.main, name = 'main'),
    url(r'', views.fetch_paste, name = 'fetch_paste'),
]
