"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from polls import views as polls_views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'',include('polls.urls')),
    path('contact/', include('contact.urls'), name='contactsite'),
    path('registration/', include('registration.urls'), name='register'),
    path('search/', include('search.urls'), name='searchsite'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
