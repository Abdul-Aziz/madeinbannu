from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'slug')
    prepopulated_fields = {'slug': ('cat_name',)}

admin.site.register(Category,CategoryAdmin)

# Register your models here.
