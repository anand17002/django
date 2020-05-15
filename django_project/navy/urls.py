from django.urls import re_path
from . import views
from django.urls import path, include

from navy import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	re_path(r'^navy_list/$', views.NavyViews.as_view(), name="navy_list"),

]