from django.contrib import admin
from django.urls import path
from blog.views import PostViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostViews.as_view(), name='home'),
]