from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from core import serializers as UserSerializers
from spotlight import models

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = "__all__"



class PostSerializer(serializers.ModelSerializer):
    user = UserSerializers.UserSerializer()
    category = CategorySerializer()
    all_tags = serializers.SerializerMethodField(read_only = True)
    images = serializers.SerializerMethodField(read_only = True)
    files = serializers.SerializerMethodField(read_only = True)
    reacts = serializers.SerializerMethodField(read_only = True)
    comments = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = models.Post
        fields = "__all__"

    def get_images(self, obj):
        images = models.PostImage.objects.filter(post = obj)
        data = PostImageSerializer(images, many=True).data
        return data

    def get_files(self, obj):
        files = models.PostFile.objects.filter(post = obj)
        data = PostFileSerializer(files, many=True).data
        return data

    def get_reacts(self, obj):
        reacts = models.PostReact.objects.filter(post = obj)
        data = PostReactSerializer(reacts, many=True).data
        return data

    def get_comments(self, obj):
        comments = models.PostComment.objects.filter(post = obj)
        data = PostCommentSerializer(comments, many=True).data
        return data

    def get_all_tags(self, obj):
        tags = obj.tags.all()
        data = TagSerializer(tags, many=True).data
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
    user = UserSerializers.UserSerializer()
    replies = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = models.PostComment
        fields = "__all__"

    def get_replies(self, obj):
        replies = models.PostCommentReply.objects.filter(comment = obj)
        data = PostCommentReplySerializer(replies, many=True).data
        return data


class PostCommentReplySerializer(serializers.ModelSerializer):
    user = UserSerializers.UserSerializer()

    class Meta:
        model = models.PostCommentReply
        fields = "__all__"


