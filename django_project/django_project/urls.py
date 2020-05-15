

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from navy import views as users_views
#from subject import views as subject_views
from django.conf import settings
#from django.conf.urls.static import static
#from rest_framework.schemas.coreapi import AutoSchema


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',users_views.EmptyView.as_view()),
    path('navy/', include('navy.urls')),
    path('', include('contact.urls')),
    #path('contact/', include('contact_form.urls')),
    path('',TemplateView.as_view(template_name='navy/home.html')),
    path('', include('blog.urls')),
    #path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    path('rooms/', include('rooms.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    

    ]