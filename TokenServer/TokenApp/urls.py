from django.urls import path

from . import views

urlpatterns = [
    path('register-client/', views.RegisterNewUser.as_view()),
    path('show-client-list/', views.ShowClientList.as_view()),
    path('authorize-client/', views.AuthorizeClient.as_view()),
]