from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django.db.models import Q


from spotlight import models, serializers
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        query_set = models.Category.objects.all()

        search = self.request.query_params.get('search', None)
        if search:
            query_set = query_set.filter(title__icontains=search)

        return query_set

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_queryset(self):
        query_set = models.Post.objects.all()
        search = self.request.query_params.get('search', None)
        if search:
            query_set = query_set.filter(description__icontains=search)

        order_by = self.request.query_params.get('orderby', None)
        if order_by:
            if order_by == "recent":
                query_set = query_set.orderby('-date')

        return query_set

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


    @action(detail=False, methods=['get'], permission_classes=[permissions.AllowAny])
    def my_properties(self, request, pk=None):
        serializer_context = {
            'request': request,
        }
        queryset = self.get_queryset()
        data = serializers.PostSerializer(queryset, many = True, context = serializer_context)
        return Response(data)


class PostReactViewSet(viewsets.ModelViewSet):
    queryset = models.PostReact.objects.all()
    serializer_class = serializers.PostReactSerializer

    def get_permissions(self):
        if self.action in ('list', 'create'):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = models.PostComment.objects.all()
    serializer_class = serializers.PostCommentSerializer

    def get_permissions(self):
        if self.action in ('list', 'create'):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class PostCommentReplyViewSet(viewsets.ModelViewSet):
    queryset = models.PostCommentReply.objects.all()
    serializer_class = serializers.PostCommentReplySerializer

    def get_permissions(self):
        if self.action in ('list', 'create'):
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]