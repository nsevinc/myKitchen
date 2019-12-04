from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.contrib import messages
from django import forms
from myKitchen.models import Locations,Quantity_Units,Material_Groups
from django.utils import timezone
from .forms import LocationsForm,Quantity_UnitsForm,Material_GroupForm
from django.views.generic import UpdateView
from django.utils.translation import gettext_lazy,activate, get_language_info

#from django.views import generic
#from django.http import HttpResponse
#from django.shortcuts import get_object_or_404
    
def index(request):
    return render(request, 'myKitchen/index.html')

## Material Groups
def material_groups_view(request):  
    #from django.utils import translation
    #user_language = 'en'
    #translation.activate(user_language)
    #request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    material_groups = Material_Groups.objects.all()
    return render(request, 'myKitchen/material_groups/mgroups.html', {'material_groups': material_groups})

def material_groups_new_view(request):
    form = Material_GroupForm
    if request.method == 'POST':
        form = Material_GroupForm(request.POST)
        if request.POST.get('name'):
            post=Material_Groups()
            post.name= request.POST.get('name')
            post.stext= request.POST.get('stext')
            post.createdat= timezone.now()
            post.save()
            
            return redirect('/materialgroups/') 
    else: 
        return render(request, 'myKitchen/material_groups/mgroups_new.html',{'form': form})

class material_groups_edit_view(UpdateView):
    model = Material_Groups
    form_class = Material_GroupForm
    template_name = "myKitchen/material_groups/mgroups_new.html"

    def get_object(self, *args, **kwargs):
        material_groups = get_object_or_404(Material_Groups, pk=self.kwargs['pk'])
        return material_groups

    def get_success_url(self, *args, **kwargs):
        return reverse(material_groups_view)  
    
def material_groups_delete_post(request, pk):
    try:
       post = Material_Groups.objects.all().filter(pk=pk)
       post.delete()
    except Exception as e:
        messages.warning(request,'Hata oluştu. Hata:{}'.format(e))
    
    return redirect('/materialgroups/') 

## Quantity Units
def qunits_view(request):  
    qunits_list = Quantity_Units.objects.all()
    return render(request, 'myKitchen/qunits/qunits.html', {'qunits_list': qunits_list})

def qunits_new_view(request):
    form = Quantity_UnitsForm
    if request.method == 'POST':
        form = Quantity_UnitsForm(request.POST)
        if request.POST.get('name'):
            post=Quantity_Units()
            post.name= request.POST.get('name')
            post.stext= request.POST.get('stext')
            post.createdat= timezone.now()
            post.save()
            
            return redirect('/qunits/') 
    else: 
        return render(request, 'myKitchen/qunits/qunits_new.html',{'form': form})

class qunits_edit_view(UpdateView):
    model = Quantity_Units
    form_class = LocationsForm
    template_name = "myKitchen/qunits/qunits_new.html"

    def get_object(self, *args, **kwargs):
        quantity_units = get_object_or_404(Quantity_Units, pk=self.kwargs['pk'])
        return quantity_units

    def get_success_url(self, *args, **kwargs):
        return reverse(qunits_view)  
    
def qunits_delete_post(request, pk):
    try:
       post = Quantity_Units.objects.all().filter(pk=pk)
       post.delete()
    except Exception as e:
        messages.warning(request,'Hata oluştu. Hata:{}'.format(e))
    
    return redirect('/qunits/') 
    
## Locations 
def locations_view(request):  
    location_list = Locations.objects.all()
    return render(request, 'myKitchen/locations/locations.html', {'location_list': location_list})


def locations_new_view(request):
    form = LocationsForm
    if request.method == 'POST':
        form = LocationsForm(request.POST)
        if request.POST.get('name'):
            post=Locations()
            post.name= request.POST.get('name')
            post.stext= request.POST.get('stext')
            post.createdat= timezone.now()
            post.save()
            
            return redirect('/locations/') 
    else: 
        return render(request, 'myKitchen/locations/locations_new.html',{'form': form})
    
class locations_edit_view(UpdateView):
    model = Locations
    form_class = LocationsForm
    template_name = "myKitchen/locations/locations_new.html"

    def get_object(self, *args, **kwargs):
        locations = get_object_or_404(Locations, pk=self.kwargs['pk'])
        return locations

    def get_success_url(self, *args, **kwargs):
        return reverse(locations_view)  
    
def locations_delete_post(request, pk):
    try:
       post = Locations.objects.all().filter(pk=pk)
       post.delete()
    except Exception as e:
        messages.warning(request,'Hata oluştu. Hata:{}'.format(e))
    
    return redirect('/locations/') 

#def locations_edit_view2(request, pk):# iptal edildi
#    try:
#       post = Locations.objects.all().filter(pk=pk)
#       post.name= request.POST.get('name')
#       post.stext= request.POST.get('stext')
#       post.save()
       
#    except Exception as e:
#        messages.warning(request,'Hata oluştu. Hata:{}'.format(e))
    
#    return redirect('/locations/') 



            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
