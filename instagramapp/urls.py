from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.homepage,name = 'home'),
    url(r'search/', views.search, name='search'),
    url(r'signup/', views.signup, name='signup'),
    url(r'profile',views.show_profile, name='profile'),
    url(r'update/<id>', views.update_profile, name='update_profile'),
]