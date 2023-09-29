from django.contrib import admin

from .models import Comment, Rating


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'order', 'store', 'created_at')
    list_filter = ('store',)
    search_fields = ('name', 'content', 'order__id')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('score', 'product', 'created_at')
    list_filter = ('product', 'score')
    search_fields = ('score', 'product__name')
