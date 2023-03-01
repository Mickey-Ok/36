
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('', include('OceanApp.urls')), 
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
   # path('books/', include('books.urls')),
    path('authentication/',include('django.contrib.auth.urls')),
  
]


