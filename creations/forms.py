from django import forms

class contactForm(forms.Form):
    subject = forms.CharField(label='Subject ',max_length=100)
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label ="Email", max_length=100)
    msg = forms.CharField(label="Message",widget=forms.Textarea)
