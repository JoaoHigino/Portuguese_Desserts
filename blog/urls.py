from . import views
from django.urls import path, reverse
from django.views.generic import TemplateView
from django.urls import path
from django.contrib import admin
from sampleapp.views import register


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        'about',
        views.generic.TemplateView.as_view(template_name='about.html'),
        name='about'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('admin/', admin.site.urls),  
    path('register', register, name='register')

]
