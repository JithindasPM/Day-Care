from django.urls import path
from AdminSide import views

urlpatterns=[
    path('Index/',views.Index,name="Index"),
    path('Registration/',views.Registration,name="Registration"),
    path('Admin_registration/',views.Admin_registration,name="Admin_registration"),
    path('Logout_Admin/',views.Logout_Admin,name="Logout_Admin"), 

    path('Login/',views.Login,name="Login"),
    path('login_save/',views.login_save,name="login_save"),
    path('Drivers_List/',views.Drivers_List,name="Drivers_List"),
    path('Single_Driver/<int:infoid>',views.Single_Driver,name="Single_Driver"),
    path('Driver_Revert_Updation/<int:dataid>',views.Driver_Revert_Updation,name="Driver_Revert_Updation"),
    path('Delete_driver/<int:dataid>',views.Delete_driver,name="Delete_driver"),
    path('Add_vehicle/',views.Add_vehicle,name="Add_vehicle"),
    path('Save_Vehicle/',views.Save_Vehicle,name="Save_Vehicle"),


    path('StaffList/',views.StaffList,name="StaffList"),
    path('Staff_Registration/',views.Staff_Registration,name="Staff_Registration"),
    path('StaffLogin/',views.StaffLogin,name="StaffLogin"),
    path('Save_staff/',views.Save_staff,name="Save_staff"),
    path('Staff_Login_Page/',views.Staff_Login_Page,name="Staff_Login_Page"),
    path('StaffDashboard/',views.StaffDashboard,name="StaffDashboard"),
    path('Staff_Profile/',views.Staff_Profile,name="Staff_Profile"),
    path('Staff_Logout/',views.Staff_Logout,name="Staff_Logout"),
    path('Single_Staff/<int:dataid>',views.Single_Staff,name="Single_Staff"),
    path('Update_Staff_Status/<int:dataid>',views.Update_Staff_Status,name="Update_Staff_Status"),
    path('Update_Staff_Password/<int:dataid>',views.Update_Staff_Password,name="Update_Staff_Password"),
    path('Delete_Staff/<int:dataid>',views.Delete_Staff,name="Delete_Staff"),
    

    path('addPlans/',views.addPlans,name="addPlans"),
    path('Save_plan/',views.Save_plan,name="Save_plan"),
    path('Edit_Plan/<int:infoid>',views.Edit_Plan,name="Edit_Plan"),
    path('Delete_Plan/<int:infoid>',views.Delete_Plan,name="Delete_Plan"),
    path('Update_plan/<int:infoid>',views.Update_plan,name="Update_plan"),
    path('Display_plans/',views.Display_plans,name="Display_plans"),

    path('Children_display/',views.Children_display,name="Children_display"),
    path('single_Children/<int:infoid>',views.single_Children,name="single_Children"),
    path('Assign_driver/<int:infoid>',views.Assign_driver,name="Assign_driver"),

]