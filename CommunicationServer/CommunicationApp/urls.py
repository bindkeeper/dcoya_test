from django.urls import path

from . import views


urlpatterns = [
    path('echo/', views.Echo.as_view()),
    path('time/', views.Time.as_view()),
]
