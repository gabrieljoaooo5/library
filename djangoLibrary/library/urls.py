from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^book_list/', book_list, name='list_books'),
]

