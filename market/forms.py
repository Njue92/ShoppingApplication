from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from products.models import Products


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ['category', 'image', 'title', 'description', 'price']


class LoginUserForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password1']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            field_names = [field_name for field_name, _ in self.fields.items()]
            for field_name in field_names:
                field = self.fields.get(field_name)
                field.widget.attrs.update({'placeholder': field.label})