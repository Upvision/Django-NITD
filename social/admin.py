from django.contrib import admin
import nested_admin

from . import models

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
    list_display = ['id', 'description', 'datetime']
    list_display_links = ['id', 'description', 'datetime']
    search_fields = ['description']

# Register your models here.

admin.site.register(models.Post,PostAdmin)