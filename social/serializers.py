from django.urls import path, include
from social import models
from rest_framework import routers, serializers, viewsets
from student.serializers import StudentSerializer


class PostSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    description = serializers.TextField()
    datetime = serializers.DateTimeField()
    class Meta:
        model = models.Post
        fields = "__all__"

    def create(self, validated_data):
        return models.Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.student = validated_data.get('student', instance.student)
        instance.description = validated_data.get('description', instance.description)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.save()
        return instance

class PostImageSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    image = serializers.ImageField()
    class Meta:
        model = models.PostImage
        fields = "__all__"
    def create(self, validated_data):
        return models.PostImage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.post = validated_data.get('post', instance.post)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

class PostFileSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    image = serializers.FileField()
    video = serializers.BooleanField()
    class Meta:
        model = models.PostFile
        fields = "__all__"
    def create(self, validated_data):
        return models.PostFile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.post = validated_data.get('post', instance.post)
        instance.image = validated_data.get('image', instance.image)
        instance.video = validated_data.get('video', instance.video)
        instance.save()
        return instance

class PostReactSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    student = StudentSerializer()
    type  = models.CharField()
    datetime = serializers.DateTimeField()
    class Meta:
        model = models.PostReact
        fields = "__all__"
    def create(self, validated_data):
        return models.PostReact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.post = validated_data.get('post', instance.post)
        instance.student = validated_data.get('student', instance.student)
        instance.type = validated_data.get('type', instance.type)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.save()
        return instance

class PostCommentSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    student = StudentSerializer()
    comment  = models.TextField()
    datetime = serializers.DateTimeField()
    class Meta:
        model = models.PostComment
        fields = "__all__"
    def create(self, validated_data):
        return models.PostComment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.post = validated_data.get('post', instance.post)
        instance.student = validated_data.get('student', instance.student)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.save()
        return instance

class PostCommentReplySerializer(serializers.ModelSerializer):
    comment = PostCommentSerializer()
    reply = models.TextField()
    datetime = serializers.DateTimeField()
    class Meta:
        model = models.PostCommentReply
        fields = "__all__"
    def create(self, validated_data):
        return models.PostReact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.reply = validated_data.get('reply', instance.reply)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.save()
        return instance

class PostShareSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    student = StudentSerializer()
    datetime = serializers.DateTimeField()
    class Meta:
        model = models.PostShare
        fields = "__all__"
    def create(self, validated_data):
        return models.PostShare.objects.create(**validated_data)
