from email.policy import default
from django import forms

class ProcessorForm(forms.Form):
    inp = forms.CharField(max_length=500, required=True)
    
    def __str__(self):
        return f"{self.inp}"
   
