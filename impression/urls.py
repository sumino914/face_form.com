from django.urls import path
from . import views

app_name = 'impression'

urlpatterns = [
    path('',views.start,name='start'),
    path('create/<int:pk>',views.impression_create,name='impression_create'),
    path('number1/<int:pk>',views.number1,name='number1'),
    path('number2/<int:pk>',views.number2,name='number2'),
    path('thanks',views.thanks,name='thanks')
]