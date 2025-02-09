

from django.urls import path
from myaccount import views
urlpatterns = [

    path('', views.ShowHomePage.as_view(), name='show-home-page'),
    path('login', views.Login.as_view(), name='login'),

]
