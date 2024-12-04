from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    
    path('signup/', views.signup, name='signup'),
    # path('accounts/login/',include("django.contrib.auth.urls")),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('home/',views.home, name='home'),
    
    #patient urls
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/update/', views.patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),

    # Doctor URLs
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/create/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/update/', views.doctor_update, name='doctor_update'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),

    #Hospital urls
    path('hospitals/',views.hospital_list,name='hospital_list'),
    path('hospitals/create/', views.hospital_create, name='hospital_create'),
    path('hospitals/<int:pk>/update/', views.hospital_update, name='hospital_update'),
    path('hospitals/<int:pk>/delete/', views.hospital_delete, name='hospital_delete'),

    #Appointments urls
    path('appointments/',views.appointment_list, name="appointment_list"),
    path('appointments/create/',views.create_appointment, name="create_appointment"),
    path('appointments/<int:pk>/update',views.update_appointment, name="update_appointment"),
    path('appointments/<int:pk>/delete',views.delete_appointment, name="delete_appointment"),

]