from django.urls import path
from .views import Signupuser, Loginuser, Logout, MedicineList, MedicineDetail,CreateMedicine

urlpatterns = [
    path('apisignup/', Signupuser.as_view(), name='apisignup'),
    path('apilogin/', Loginuser.as_view(), name='apilogin'),
    path('apilogout/', Logout.as_view(), name='apilogout'),
    path('apimedicines/', MedicineList.as_view(), name='apimedicinelist'),
    path('apimedicines/create/', CreateMedicine.as_view(), name='apicreatemedicine'),
    path('apimedicines/<int:pk>/', MedicineDetail.as_view(), name='apimedicinedetail'),
]