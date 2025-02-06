

from django.urls import path
from account import views
urlpatterns = [

    path('', views.ShowHomePage.as_view(), name='show-home-page'),
    path('login', views.Login.as_view(), name='login'),

]
