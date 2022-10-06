from django.urls import path

from .views import list_equipos, ListEquipoGenericView

urlpatterns = [
    path('lista-equipos/',list_equipos ,name='lista-equipos'),
    # path('class-view/lista-equipos/',ListEquipoGenericView.as_view() ,name='lista-equipos-class-view'),
]