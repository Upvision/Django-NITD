from django.urls import path, include
from social import models
from rest_framework import routers, serializers, viewsets
from student.serializers import StudentSerializer


class PostSerializer(serializers.ModelSerializer):
    # student = StudentSerializer()
    # description = serializers.TextField()
    images = serializers.SerializerMethodField(read_only=True)
    files = serializers.SerializerMethodField(read_only=True)
    reacts = serializers.SerializerMethodField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Post
        fields = "__all__"

    def get_images(self, obj):
        images = models.PostImage.objects.filter(post=obj)
        data = PostImageSerializer(images, many=True).data
        return data

    def get_files(self, obj):
        files = models.PostFile.objects.filter(post=obj)
        data = PostFileSerializer(files, many=True).data
        return data

    def get_reacts(self, obj):
        reacts = models.PostReact.objects.filter(post=obj).count()
        return reacts

    def get_comments(self, obj):
        comments = models.PostComment.objects.filter(post=obj)
        data = PostCommentSerializer(comments, many=True).data
        return data

class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostImage
        fields = "__all__"

class PostFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostFile
        fields = "__all__"

class PostReactSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostReact
        fields = "__all__"


class PostCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.PostComment
        fields = "__all__"

    def get_replies(self, obj):
        replies = models.PostCommentReply.objects.filter(comment = obj)
        data = PostCommentReplySerializer(replies, many=True).data
        return data

class PostCommentReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostCommentReply
        fields = "__all__"

class PostShareSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PostShare
        fields = "__all__"