from django.contrib import admin
from .models import Category, Tag, Image, Article

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Image)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','category')
    list_filter = ('author','category','status')
    search_fields = ('title','author__username','category__name')
    date_hierarchy = 'publish_date'
    ordering = ('created_at','publish_date')