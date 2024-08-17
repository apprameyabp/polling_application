from . import views
from django.urls import path


urlpatterns = [
    path("",views.basic_view,name='index'),
]
