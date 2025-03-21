from django.urls import path
from CareApp import views
import DriverApp.urls

urlpatterns=[
    path('Children_Form/',views.Children_Form,name="Children_Form"),
    path('',views.Home,name="Home"),
    path('About/',views.About,name="About"),
    path('Profile/',views.Profile,name="Profile"),
    path('ParentsLogin/',views.ParentsLogin,name="ParentsLogin"),
    path('Registration_save/',views.Registration_save,name="Registration_save"),
    path('Parents_Login_save/',views.Parents_Login_save,name="Parents_Login_save"),
    path('Update_Registration/<int:infoid>',views.Update_Registration,name="Update_Registration"),
    path('Parents_Logout/',views.Parents_Logout,name="Parents_Logout"),
    path('Update_Route/<int:dataid>',views.Update_Route,name="Update_Route"),
    path('View_Plans/',views.View_Plans,name="View_Plans"),
    path('rating_save/',views.rating_save,name="rating_save"),
    path('Payment_pg/<int:dataid>',views.Payment_pg,name="Payment_pg"),
    path('Payment_save/',views.Payment_save,name="Payment_save"),
    # path('Purchase_List/',views.Purchase_List,name="Purchase_List"),



]

