from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path(r'',views.homepage,name = 'home'),
    path(r'search/', views.search, name='search'),
    path(r'signup/', views.signup, name='signup'),
    path(r'profile',views.show_profile, name='profile'),
    path(r'update/<id>', views.update_profile, name='update_profile'),
    path('posts/',views.new_post, name='post'),
    path('comment/<id>', views.comment, name='comment')
]