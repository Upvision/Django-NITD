from django.contrib import admin
import nested_admin
# Register your models here.
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title',]
    list_display_links = ['id','title',]
    list_filter = []
    search_fields = ['title',]

class TagAdmin(admin.ModelAdmin):
    list_display = ['id','title',]
    list_display_links = ['id','title',]
    list_filter = []
    search_fields = ['title',]

class FilesInlineAdmin(nested_admin.NestedTabularInline):
    model = models.PostFile
    extra = 1


class ImagesInlineAdmin(nested_admin.NestedTabularInline):
    model = models.PostImage
    extra = 1


class ReactInlineAdmin(nested_admin.NestedTabularInline):
    model = models.PostReact
    extra = 0

class CommentReplyInlineAdmin(nested_admin.NestedTabularInline):
    model = models.PostCommentReply
    extra = 1

class CommentInlineAdmin(nested_admin.NestedTabularInline):
    model = models.PostComment
    inlines = [CommentReplyInlineAdmin]
    extra = 0

class PostAdmin(nested_admin.NestedModelAdmin):
    inlines = [ImagesInlineAdmin, FilesInlineAdmin, CommentInlineAdmin, ReactInlineAdmin ]
    list_display = ['id', 'category', 'title', 'datetime']
    list_display_links = ['id', 'category', 'title', 'datetime']
    list_filter = ['category', 'tags']
    search_fields = ['title', 'description']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Post, PostAdmin)