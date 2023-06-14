from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_form, name="login_form"),
    path('home/', views.index_page, name= "home"),
    path('choices/', views.choices_page, name= "choices"),
    path('query/', views.query_system, name = "query"),
    path('logout/', views.logout_user, name = "logout")
]
