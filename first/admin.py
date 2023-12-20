# yourapp/admin.py

from django.contrib import admin
from .models import Category, SubCategory, Like, Comment, Product, ProductSize, ProductColor,FirstCart

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    search_fields = ('name',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at',)
    search_fields = ('user__username', 'product__title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'text', 'created_at',)
    search_fields = ('user__username', 'product__title', 'text',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'subcategory', 'price', 'brand', 'like_count', 'comment_count',)
    list_filter = ('category', 'subcategory', 'brand',)
    search_fields = ('title', 'brand',)

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)

@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('color',)

admin.site.register(FirstCart)
