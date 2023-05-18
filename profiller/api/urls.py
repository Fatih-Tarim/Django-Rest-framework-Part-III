from django.urls import path
from profiller.api.views import ProfilViewSet

profil_list = ProfilViewSet.as_view({'get':'list'})
profil_detay = ProfilViewSet.as_view({'get':'retrieve'})

urlpatterns = [
    path('kullanici-profilleri/', profil_list, name='profiller'),
    path('kullanici-profilleri/<int:pk>', profil_detay, name='profil-detay'),
]
