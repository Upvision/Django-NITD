from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
import rest_framework

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('_nested_admin/', include('nested_admin.urls')),

    # path('core/', include('core.urls', namespace='core')),
    path('docs/', include_docs_urls(title='NIT Delhi')),
    path('student/', include('student.urls', namespace='student')),
    path('spotlight/', include('spotlight.urls', namespace='spotlight')),
    path('social/', include('social.urls', namespace='social')),

]
