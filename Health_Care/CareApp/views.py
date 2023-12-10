from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientForm, VendorForm
from .models import Patient, Doctor
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def HomePage(request):
    return render(request, 'index.html')

def logoutuser(request):
    return render(request, 'registration/signout.html')

def Add_Appointment(request):
    form = PatientForm
    patient_dict = {'form': form}

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return HomePage(request)
    return render(request, 'appointment/add_appointment.html', patient_dict)

def Appointment_Report(request):
    information = Patient.objects.all()
    context = {'patients': information}
    return render(request, 'appointment/appointment_report.html', context)


def Update_Patient(request, id):
    p = Patient.objects.get(id=id)
    form = PatientForm(instance=p)
    dict = {'form': form}

    if request.method == 'POST':
        form = PatientForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
        return Appointment_Report(request)
    return render(request, 'appointment/Update_appointment.html', dict)

def Delete_Patient(request, id):
    p = Patient.objects.get(id=id)
    p.delete()
    return Appointment_Report(request)


def NewVendor(request):
    form = VendorForm
    vendor_dict = {'form': form}
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['contact'])
            print(form.cleaned_data['item'])
        return HomePage(request)
    return render(request, 'appointment/vendor.html', vendor_dict)



class ClassBasedView(View):
    def get(self, request):
        return HttpResponse('<h1>Welcome To ClassBasedViews,,!</h1>')


class DoctorsList(ListView):
    model = Doctor
    template_name = 'appointment/doctor_list.html'


class DoctorDetail(DetailView):
    model = Doctor
    template_name = 'appointment/doctor_detail.html'


class AddDoctor(CreateView):
    model = Doctor
    fields = ['id', 'name', 'designation', 'specialist', 'contact']
    template_name = 'appointment/doctor_form.html'


class UpdateDoctor(UpdateView):
    model = Doctor
    fields = ['id', 'name', 'designation', 'specialist', 'contact']
    template_name = 'appointment/doctor_form.html'


class DeleteDoctor(DeleteView):
    model = Doctor
    template_name = 'appointment/doctor_conform_delete.html'
    success_url = reverse_lazy('doctorlist')

