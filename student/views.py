from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status
from django.db.models import Q

from student import models, serializers



class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def get_queryset(self):
        query_set = models.Student.objects.all()

        search = self.request.query_params.get('search', None)
        if search:
            query_set = query_set.filter(Q(full_name__icontains=search) | Q(intro__icontains = search))

        return query_set