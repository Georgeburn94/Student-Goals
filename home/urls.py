from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('responses', views.responses, name='responses'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)