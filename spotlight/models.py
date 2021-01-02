from django.db import models

class Category(models.Model):
    title = models.CharField(max_length = 256)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Category"

class Tag(models.Model):
    title = models.CharField(max_length = 256)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tags"

class Post(models.Model):
    category = models.ForeignKey('spotlight.Category', on_delete = models.CASCADE)
    user = models.ForeignKey('core.User', on_delete = models.CASCADE, related_name="spotlight_user_post" )
    tags = models.ManyToManyField('spotlight.Tag')
    title = models.CharField(max_length = 512)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default= False)
    image = models.ImageField(null=True)

class PostImage(models.Model):
    post = models.ForeignKey('spotlight.Post', on_delete = models.CASCADE )
    image = models.ImageField()

class PostFile(models.Model):
    post = models.ForeignKey('spotlight.Post', on_delete = models.CASCADE )
    file = models.FileField()
    video = models.BooleanField(default = False)


Post_React_Choices = (
    ("Like", "Like"),
    ("Celebrate", "Celebrate"),
)
class PostReact(models.Model):
    post = models.ForeignKey('spotlight.Post', on_delete = models.CASCADE )
    user = models.ForeignKey('core.User', on_delete = models.CASCADE, related_name = "spotlight_react_user")
    type = models.CharField(max_length = 10, choices = Post_React_Choices )
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Post Reacts"
        unique_together = ['post', 'user']

class PostComment(models.Model):
    post = models.ForeignKey('spotlight.Post', on_delete=models.CASCADE)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name = "spotlight_user_comment")
    comment = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

class PostCommentReply(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name = "spotlight_user_reply")
    comment = models.ForeignKey('spotlight.PostComment', on_delete = models.CASCADE)
    reply = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Post Comment Replies"

