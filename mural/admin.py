from django.contrib import admin
from .models import Category, Mural

# Register your models here


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)

@admin.register(Mural)
class MuralAdmin(admin.ModelAdmin):
    ...