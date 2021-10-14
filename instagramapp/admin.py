from django.contrib import admin
from instagramapp.models import Comment, Image, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)