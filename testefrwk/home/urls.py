
from django.urls import path
from .views import home,my_logout
from django.urls import path, include


urlpatterns = [
    path('', home,name = "home"),
    path('logout/', my_logout,name = "my_logout"),
    path('login/', include('django.contrib.auth.urls')),
]

