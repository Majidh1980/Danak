from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about, name='about'),
    path('tutorials/', views.tutorials, name='tutorials'),
    path('blog/', views.blog, name='blog'),
    path('contact_us/', views.contact_us, name='contact_us'),
]