from django.contrib import admin

# Register your models here.
from . models import Category,Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cname','slug']
    prepopulated_fields = {'slug':('cname',)}


admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','balance','created','updated']
    list_editable = ['price','stock','balance']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Product, ProductAdmin)