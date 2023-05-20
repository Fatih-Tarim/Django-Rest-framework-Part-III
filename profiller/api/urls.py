from django.urls import path, include
from profiller.api.views import ProfilViewSet, ProfilDurumViewSet, ProfilFotoUpdateView
from rest_framework.routers import DefaultRouter

# profil_list = ProfilViewSet.as_view({'get':'list'})
# profil_detay = ProfilViewSet.as_view({'get':'retrieve'})

router = DefaultRouter()
router.register(r'profiller',ProfilViewSet)
router.register(r'durum',ProfilDurumViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('profil-foto/', ProfilFotoUpdateView.as_view(), name='profil-foto '),
]
