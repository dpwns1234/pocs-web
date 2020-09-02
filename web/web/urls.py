"""web URL Configuration

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
from django.urls import include, path
from django.contrib.auth.views import LoginView
from webpage.views import index
import webpage.views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include([
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login')
    ])),

    path('', index),
    path('cafeMain/', webpage.views.cafeMain, name='cafeMain'),
    path('createWrite/', webpage.views.createWrite, name='createWrite'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('cafeMain/detail/', webpage.views.detail, name='detail'),
    path('cafeMain/detail/<int:write_id>/', webpage.views.detail, name='detail'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
