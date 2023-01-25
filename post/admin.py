from django.contrib import admin
from .models import Category, Tag, Post, Rating


admin.site.register(Category)
# admin.site.register(Tag)
# admin.site.register(Post)
# admin.site.register(Rating)

class RatingInline(admin.TabularInline):
    model = Rating

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'category', 'get_rating')
    inlines = [RatingInline]
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title', )}
    ordering = ['-created_at']
    list_filter = ['category__title']

    def get_rating(self, obj):
        from django.db.models import Avg
        result = obj.ratings.aggregate(Avg('rating'))
        return result['rating__avg']