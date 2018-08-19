
from django.contrib import admin
from django.urls import path,re_path,include
from django.contrib.auth import views as auth_views
from myapp import views



urlpatterns = [

    re_path(r'^login/$',auth_views.LoginView.as_view, name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view, name='logout'),
    re_path(r'', include('social_django.urls', namespace='social')),
    path('',include('myapp.urls')),
    path('admin/', admin.site.urls),
    path('accounts/profile/',views.page),



]
