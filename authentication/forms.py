from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import ApplicationForm

class ApplicationForm (forms.ModelForm):
    class Meta:
        model=ApplicationForm
        fields='__all__'



# class ProductCreateForm(forms.ModelForm):
#     image = forms.ImageField()
#     class Meta:
#         model = Product
#         fields = ('category', 'name', 'price', 'description', 'image', 'stock', 'available', 'slug')

#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url

# class ClientSignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=100, required=True)
#     last_name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(max_length=250, help_text='eg. youremail@gmail.com')
#     id_number = forms.CharField(max_length=13, required=True)
#     phone = forms.CharField(max_length=15, required=True)
   
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'id_number', 'phone',),

    
