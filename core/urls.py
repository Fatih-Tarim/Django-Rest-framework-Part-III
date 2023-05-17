from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include('rest_framework.urls')), #Browsable api sayfası için
    path('api/rest-auth/', include('dj_rest_auth.urls')), #dj-rest-auth ile gelen endpointler için
    path("api/", include('profiller.api.urls')),
]


#################################
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

