from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rizotto', views.recipe1, name='recipe_rizotto'),
    path('ravioli', views.recipe2, name='recipe_ravioli'),
    path('carbonara', views.recipe3, name='recipe_carbonara'),
    path('balaneza', views.recipe4, name='recipe_balaneza'),
    path('lazania', views.recipe5, name='recipe_lazania'),
    path('porcketa', views.recipe6, name='recipe_porcketa'),
]