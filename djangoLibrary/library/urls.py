from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^book_list/', book_list, name='book_list'),
    url(r'^book_new/', book_new, name='book_new'),
    url(r'^book_edit/(?P<pk>[0-9]+)', book_edit, name='book_edit'),
]

