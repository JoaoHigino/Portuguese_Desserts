from . import views
from django.urls import path, reverse
from django.views.generic import TemplateView


urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='post_like'),
    path(
        'about',
        views.generic.TemplateView.as_view(template_name='about.html'),
        name='about'),
    path('search_articles', views.search_articles, name='search_articles'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='details'),
]
