
from django.contrib import admin
from django.urls import path,include,re_path
from . import views
app_name='myapp'
urlpatterns = [

    path('',views.login),
    path('list/',views.contact),
    path('snippet/',views.Snippet_details),
    path('list/<int:id>', views.detail),
    path('snippet/go_back',views.homes),
    path('list/<int:id>/add',views.price_increase),
    path('list/<int:id>/decrease',views.price_decrease),
    path('list/<int:id>/go_back',views.home),
    path('list/1/pay', views.payment, name='payment'),
    re_path(r'^response/', views.response, name='response'),
]
