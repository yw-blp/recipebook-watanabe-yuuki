from django.urls import path
from .views import (RecipeListView, RecipeCreateView, RecipeDetailView,
                    RecipeImageCreateView)

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/<int:pk>/add_image', RecipeImageCreateView.as_view(),
         name='recipe-update-add-image'),
]

app_name = 'ledger'
