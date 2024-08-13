# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import UserRegistration


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = UserRegistration
#         fields = UserCreationForm.Meta.fields + ('name', 'class1', 'email', 'mobNo', 'age')

# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = UserRegistration
#         # fields = list(getattr(UserChangeForm.Meta, 'fields', ())) + ['name', 'class1', 'email', 'mobNo', 'age']
#         # fields = UserChangeForm.Meta+ ('name', 'class1', 'email', 'mobNo', 'age')
#         print(type( UserChangeForm.Meta))