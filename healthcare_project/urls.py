from django.contrib import admin
from django.urls import path
from disease_prediction import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.predict_view, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('predict/', views.predict_view, name='predict'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] 