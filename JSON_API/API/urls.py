from django.urls import path
from . import views

urlpatterns = [
    path('PD/', views.PdView.as_view()),
    path('CLDR/', views.CldrView.as_view()),
    path('DOCU/', views.DocuView.as_view()),
    path('PINS/', views.PinsView.as_view()),
    path('PVL/', views.PvlView.as_view()),
    path('RUN/', views.RunView.as_view()),
    path('ZM/', views.ZmView.as_view()),
    path('ZUO/', views.ZuoView.as_view()),
]