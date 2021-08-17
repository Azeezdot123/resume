from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(label='', widget= forms.EmailInput(attrs={'class': 'k', 'placeholder': 'Enter the message here...'}))

    subject = forms.CharField(label='', 
    widget=forms.TextInput(attrs={'class': 'k', 'placeholder': 'Enter the Subject here...'}))

    content = forms.CharField(label='', 
    widget=forms.Textarea(attrs={'class': 'k', 'placeholder': 'Enter the message here...'}))