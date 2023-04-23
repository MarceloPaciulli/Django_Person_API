from django.urls import path
from django_application.views import index, PersonaList, PersonaDetail, PersonaUpdate, PersonaDelete, PersonCreateView
from django.conf import settings
from django.conf.urls.static import static
from django_application.views import person_success


urlpatterns = [
    path('', index, name='index'),
    path('api/personas/', PersonaList.as_view(), name='personas_list'),
    path('api/personas/<int:pk>/', PersonaDetail.as_view(), name='personas_detail'),
    path('api/personas/create/', PersonCreateView.as_view(), name='personas_create'),
    path('api/personas/update/<int:pk>/', PersonaUpdate.as_view(), name='personas_update'),
    path('api/personas/delete/<int:pk>/', PersonaDelete.as_view(), name='personas_delete'),
    path('person/success/', person_success, name='person_success'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
