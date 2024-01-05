
#from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',include('mediapp.urls')),
    path('medicoAPI/',include('medicoAPI.urls'))

   

]
