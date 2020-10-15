from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.PostImage)
admin.site.register(models.PostFile)
admin.site.register(models.PostReact)
admin.site.register(models.PostComment)
admin.site.register(models.PostCommentReply)
admin.site.register(models.PostShare)