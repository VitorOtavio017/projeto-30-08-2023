from django.contrib import admin
from .models import Category, Mural

# Register your models here


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)

class MuralAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'is_published']
    list_display_links = 'title', 'created_at'
    search_fields = 'id', 'title', 'description', 'description', 'review'
    list_filter = 'categoria', 'usuario', 'is_published'
    list_per_page = 10
    list_editable = 'is_published',
    ordering = 'id',
    prepopulated_fields = {
        "description": ('title',)
    }

admin.site.register(Mural,MuralAdmin)