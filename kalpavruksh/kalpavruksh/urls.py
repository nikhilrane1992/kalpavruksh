from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^get/questions/$', questions),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
