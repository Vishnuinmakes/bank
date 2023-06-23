from django.urls import path,include
from . import views

app_name='bank_app'

urlpatterns = [

    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/' ,views.register ,name='register'),
    path('login/application/',views.application, name='application'),
    path('login/application/form/',views.form, name='form'),
    path('login/application/form/message', views.message, name='message'),

]