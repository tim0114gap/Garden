from django import forms

class SentMaill(forms.Form):
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'contact-email','placeholder':'Email','type':'text'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class':'contact-subject','placeholder':'Subject'}),required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Message'}))

class register(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password','placeholder':'password'}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'email address','type':'text'}))
