from django import forms

class ContactFormModelForm(forms.Form):
    name= forms.CharField(label='name', max_length=100,required=True)
    email = forms.EmailField(label='email', required=True)
    message = forms.CharField(label='message', required=True,widget=forms.Textarea)