"""EORDatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from casestudies.views import TaskViewSet,CountryViewSet,JoinMiscibleCaseStudiesViewSet,JoinChemicalCaseStudiesViewSet,ListJoinMiscibleViewSet,EORTechniquesViewSet,RangepermViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router1 = routers.DefaultRouter()
# router.register(r'CaseStudies',TaskViewSet)
router.register(r'CaseStudies',ListJoinMiscibleViewSet,basename='Miscible')
router.register(r'Country',CountryViewSet)
router.register(r'EORTechniques',EORTechniquesViewSet)
router.register(r'Rangeperm',RangepermViewSet)


urlpatterns = [
    path('',include(router.urls)), 
    path('admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import url

from django.conf import settings

from django.views.static import serve

  

urlpatterns += [

  url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

  url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]