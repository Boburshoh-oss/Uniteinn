from django.urls import path
from .views import register_view,index_view,table_view,about_view

urlpatterns = [
    path('',index_view,name="index_url"),
    path('register/',register_view,name="register_url"),
    path('table',table_view,name="table_url"),
    path('about',about_view,name="about_url")
]
