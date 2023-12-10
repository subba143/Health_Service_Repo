from django.urls import path
from .views import Add_Appointment, Appointment_Report, NewVendor, Update_Patient, Delete_Patient
from .views import ClassBasedView, DoctorsList, DoctorDetail, AddDoctor, UpdateDoctor, DeleteDoctor

urlpatterns = [
    path('add/', Add_Appointment),
    path('report/', Appointment_Report),
    path('update/<int:id>', Update_Patient),
    path('delete/<int:id>', Delete_Patient),
    path('vendor/', NewVendor),
    path('cbv/', ClassBasedView.as_view()),
    path('doctorlist/', DoctorsList.as_view(), name='doctorlist'),
    path('doctordetails/<int:pk>', DoctorDetail.as_view()),
    path('adddoctor/', AddDoctor.as_view(), name='adddoctor'),
    path('updatedoctor/<int:pk>', UpdateDoctor.as_view()),
    path('deletedoctor/<int:pk>', DeleteDoctor.as_view()),

]
