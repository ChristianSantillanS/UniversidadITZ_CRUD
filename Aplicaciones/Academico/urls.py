from django.urls import path
from django.urls.resolvers import URLPattern
from.import views
urlpatterns = [
    path('',views.home),
    path('agregar/',views.agregar_a),
    path('registraralumnos/',views.registraralumnos),
    path('edicionA/<No_control>',views.edicionA),
    path('editaralumnos/',views.editaralumnos),
    path('eliminacionA/<No_control>', views.eliminacionA),
]