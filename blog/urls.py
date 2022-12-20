from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.create_recipe, name='books'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='details'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='post_like'),

]
