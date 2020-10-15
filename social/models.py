from django.db import models

# Create your models here.
class Post(models.Model):
    student = models.ForeignKey('student.Student', on_delete = models.CASCADE )
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

class PostImage(models.Model):
    post = models.ForeignKey('social.Post', on_delete = models.CASCADE )
    image = models.ImageField()

class PostFile(models.Model):
    post = models.ForeignKey('social.Post', on_delete = models.CASCADE )
    image = models.FileField()
    video = models.BooleanField(default = False)


Post_React_Choices = (
    ("Like", "Like"),
    ("Celebrate", "Celebrate"),
)
class PostReact(models.Model):
    post = models.ForeignKey('social.Post', on_delete = models.CASCADE )
    student = models.ForeignKey('student.Student', on_delete = models.CASCADE )
    type = models.CharField(max_length = 10, choices = Post_React_Choices )
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Post Reacts"
        unique_together = ['post', 'student']

class PostComment(models.Model):
    post = models.ForeignKey('social.Post', on_delete=models.CASCADE)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    comment = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

class PostCommentReply(models.Model):
    comment = models.ForeignKey('social.PostComment', on_delete = models.CASCADE)
    reply = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Post Comment Replies"

class PostShare(models.Model):
    post = models.ForeignKey('social.Post', on_delete=models.CASCADE)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add = True)
