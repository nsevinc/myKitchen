# -*- coding: utf-8 -*-

from django import forms
from .models import Locations,Quantity_Units,Material_Groups

class LocationsForm(forms.ModelForm):
    class Meta:
        model= Locations
        fields= ['name','stext']

    def save(self, id=None):
        locations = super(LocationsForm, self).save(commit=False)
        locations.save()
        return locations
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control','placeholder': 'Lokasyon Adı'})
        self.fields['name'].label = 'Lokasyon Adı'
        self.fields['stext'].widget.attrs.update({'class': 'form-control','placeholder': 'Lokasyon Açıklaması'})
        self.fields['stext'].label = 'Açıklama'
        self.fields['stext'].required = False
    
class Quantity_UnitsForm(forms.ModelForm):
    class Meta:
        model= Quantity_Units
        fields= ['name','stext']

    def save(self, id=None):
        qunits = super(Quantity_UnitsForm, self).save(commit=False)
        qunits.save()
        return qunits
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control','placeholder': 'Miktar Birim Adı'})
        self.fields['name'].label = 'Birim Adı'
        self.fields['stext'].widget.attrs.update({'class': 'form-control','placeholder': 'Miktar Birim Açıklaması'})
        self.fields['stext'].label = 'Açıklama'
        self.fields['stext'].required = False    
        
class Material_GroupForm(forms.ModelForm):
    class Meta:
        model= Material_Groups
        fields= ['name','stext']

    def save(self, id=None):
        qunits = super(Material_GroupForm, self).save(commit=False)
        qunits.save()
        return qunits
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control','placeholder': 'Malzeme Grup Adı'})
        self.fields['name'].label = 'Birim Adı'
        self.fields['stext'].widget.attrs.update({'class': 'form-control','placeholder': 'Malzeme Grup Açıklaması'})
        self.fields['stext'].label = 'Açıklama'
        self.fields['stext'].required = False           