from django.urls import path
from profiller.api.views import ProfilList

urlpatterns = [
    path('kullanici-profilleri/', ProfilList.as_view(), name='profiller'),
]
