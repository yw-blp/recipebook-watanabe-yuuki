from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile, Ingredient, Recipe, RecipeIngredient


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(BaseUserAdmin):
    search_fields = ('name', )
    inlines = [ProfileInLine, ]


class RecipeIngredientInLine(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name', 'author', 'created_on', 'updated_on')
    search_fields = ('name', )
    inlines = [RecipeIngredientInLine, ]


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name', )
    search_fields = ('name', )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
