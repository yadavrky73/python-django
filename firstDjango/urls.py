from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "Rohit Admin"
admin.site.site_title = "Rohit Admin Portal"
admin.site.index_title = "Welcome to Rohit Researcher Portal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
    # path('about', views.about, name='about'),
    # path('services',views.services, name='services'),
    # path('contact',views.contact, name='contact'),

]


