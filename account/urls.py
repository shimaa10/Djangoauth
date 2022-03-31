from django.conf.urls import url
from django.urls import path, include
from .api import LogoutApiView, RegisterApi
urlpatterns = [
      path('api/register', RegisterApi.as_view(),name='create user'),
    path('logout/', LogoutApiView.as_view(),
         name='blacklist')
]
