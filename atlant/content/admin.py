from django.contrib import admin
from .models import  BlogModel, ThemeBlogModel, AboutModel, ReviewsModel

# Register your models here.
@admin.register(ThemeBlogModel)
class ThemeBlogModelAdmin(admin.ModelAdmin):
    list_display = ('theme',)
    search_fields = ('theme',)
    list_filter =('theme',)


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'publish',)
    search_fields = ('title', 'pub_date', 'theme')
    list_filter = ('title', 'pub_date', 'theme', 'publish')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish',)
    search_fields = ('title', 'text')
    list_filter = ('title', 'text', 'publish')


@admin.register(ReviewsModel)
class ReviewsModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'publish',)
    search_fields = ('name', 'pub_date')
    list_filter = ('name', 'pub_date', 'publish')