from sem_3_1_app.views import index, about
from django.urls import path

urlpatterns = [
    path('',index, name='index'),
    path('about/',about, name='about'),

]