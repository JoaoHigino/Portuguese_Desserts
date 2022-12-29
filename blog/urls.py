from . import views
from django.urls import path, reverse
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        'about',
        views.generic.TemplateView.as_view(template_name='about.html'),
        name='about'),
    path('new', views.CreatePostView.as_view(), name='new'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path(
        'post/<slug:slug>/update/',
        views.UpdatePost.as_view(), name='post_update'
        ),
]

urlpatterns += staticfiles_urlpatterns()
