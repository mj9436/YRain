"""YRain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

import server.views

urlpatterns = [
    path('polls/', include('server.urls')),
    path('admin/', admin.site.urls),
    path('',server.views.main, name='main'),
    path('borrow/',server.views.borrow, name='borrow'),
    path('cur_status/', server.views.cur_status, name="cur_status"),
    path('borrow/dasan/', server.views.dasan, name="dasan"),
    path('borrow/yangjae/', server.views.yangjae, name="yangjae"),
]