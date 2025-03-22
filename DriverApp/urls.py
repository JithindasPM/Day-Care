from django.urls import path
from DriverApp import views

urlpatterns=[

    path('Driver_Form/',views.Driver_Form,name="Driver_Form"),
    path('Driver_Login/',views.Driver_Login,name="Driver_Login"),

    path('Driver_Registration_save/',views.Driver_Registration_save,name="Driver_Registration_save"),
    path('Driver_Login_Save/',views.Driver_Login_Save,name="Driver_Login_Save"),

    # path('Driver_Dashboard/',views.Driver_Dashboard,name="Driver_Dashboard"),
    path('Driver_Logout/',views.Driver_Logout,name="Driver_Logout"),
    path('Driver_Profile/',views.Driver_Profile,name="Driver_Profile"),
    path('Assigned_Childrens/',views.Assigned_Childrens,name="Assigned_Childrens"),
]