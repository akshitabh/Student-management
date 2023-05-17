from django.urls import path
from .import views

urlpatterns = [
    path('', views.index ),
    path('dashboard/',views.dashboard),
    path('employees/',views.employees),
    path('courses/',views.courses),
    path('signup/',views.signup),
    path('viewstudents/', views.viewstudents),
    path('registration/',views.form_data),
    path('login/',views.login),
    path('addcourse/',views.addcourses),
    path('deletecourse/<pk>/',views.deletecourse),
    
]