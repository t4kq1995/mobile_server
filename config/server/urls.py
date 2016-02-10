"""
server URL Configuration
"""
from django.conf.urls import url
from server import views

urlpatterns = [
    url(r'^$', views.show_start_page, name='login'),
]
