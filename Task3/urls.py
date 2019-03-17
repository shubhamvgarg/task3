from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from PPTFiles import views as IV
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pptfiles/', IV.Upload),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,)+static(settings.STATIC_URL)
