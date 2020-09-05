from .views import albuns_lista
from .views import album_novo
from .views import album_atualizacao
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('lista/', albuns_lista,name = "albuns_lista"),
    path('album_novo/',  album_novo,name ="album_novo"),
    path('album_atualizacao/<int:id>',  album_atualizacao,name ="album_atualizacao"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

