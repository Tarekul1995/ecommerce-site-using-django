from django.db import models
from django import forms


class Customer_Account(models.Model):
    name = models.CharField(max_length=50)
    User_Name = models.CharField(max_length=50, unique=True, error_messages={'unique': 'User Name already exist'})
    email = models.EmailField(max_length=50, unique=True, error_messages={'unique': 'e-mail already exist'})
    Address = models.CharField(max_length=150)
    contact = models.CharField(max_length=11, unique=True, error_messages={'unique': 'PhoneNumber already exist'})
    GENDER=(
        ('M','Male'),
        ('F','Female')
    )
    Gender = models.CharField(max_length=1,choices=GENDER, default='Male')
    Age = models.PositiveIntegerField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CreateCustomer(forms.ModelForm):
    re_type_pass = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Retype-password'}))

    class Meta:
        model = Customer_Account
        fields = ['name','User_Name', 'email','Address', 'Age', 'contact', 'Gender', 'password', 're_type_pass']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'User_Name': forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'E-mail'}),
            'Address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'Age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact No'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }

    def clean(self):
        cleaned_data = super(CreateCustomer, self).clean()
        if self.cleaned_data.get('password') != self.cleaned_data.get('re_type_pass'):
            raise forms.ValidationError({'password':"password doesn't match"})
        return cleaned_data

class Create_login(forms.ModelForm):

    class Meta:
        model = Customer_Account
        fields = ['User_Name', 'password']
        error_messages = {}
        widgets = {
             'User_Name': forms.TextInput(attrs={'class':'form-control','placeholder':'User_Name'}),
             'password':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
        }
    
    def clean(self):
        customer = Customer_Account.objects.get(User_Name=self.cleaned_data.get('User_Name'))
        if customer.User_Name == self.cleaned_data.get('User_Name') and customer.password == self.cleaned_data.get('password'):
            return
        else:
            raise forms.ValidationError({'E-mail or password are invalid'})