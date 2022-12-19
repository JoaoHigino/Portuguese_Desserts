from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('add-recipe/', views.create_recipe, name='add_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='details'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='post_like'),

]
