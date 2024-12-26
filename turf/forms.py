from django import forms # type: ignore
from .models import *

class Turfownregform(forms.ModelForm):
    class Meta:
        model = Turfadmin
        fields = ['name','ownername', 'gender',  'address','phone', 'email','location']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['productname','category', 'description','image','price','quantity',]

class Turfownregform(forms.ModelForm):
    slots = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Enter slots as comma-separated values (e.g., 9:00-10:00, 10:00-11:00)',
            'rows': 3
        }),
        label="Time Slots"
    )

    class Meta:
        model = Turfadmin
        fields = ['ownername', 'gender', 'address', 'phone', 'email', 'location', 'rent', 'openingtime', 'closingtime']

    def clean_slots(self):
        slots = self.cleaned_data.get('slots', '')
        if slots:
            # Validate slot format if necessary
            slot_list = [slot.strip() for slot in slots.split(',')]
            if not all(slot_list):
                raise forms.ValidationError("Please provide valid slots.")
        return slots        


    