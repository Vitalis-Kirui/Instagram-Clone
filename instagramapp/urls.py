from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.homepage,name = 'home'),
    url(r'search/', views.search, name='search'),
    url(r'signup/', views.signup, name='signup'),
    url(r'profile',views.show_profile, name='profile'),
    url(r'update/<id>', views.update_profile, name='update_profile'),
    url(r'posts/',views.new_post, name='post'),
    path('comment/<id>', views.comment, name='comment')
]