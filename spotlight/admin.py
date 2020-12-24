from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.PostReact)
admin.site.register(models.PostImage)
admin.site.register(models.PostFile)
admin.site.register(models.PostComment)
admin.site.register(models.PostCommentReply)