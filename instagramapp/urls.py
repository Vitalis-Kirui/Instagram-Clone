from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.homepage,name = 'home'),
    url(r'search/', views.search, name='search'),
    url(r'signup/', views.signup, name='signup'),
]