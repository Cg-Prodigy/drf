from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib import admin

from .models import CustomUser
# Register your models here.

class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    class Meta:
        model=CustomUser
        fields=("email","first_name","last_name")
    
    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise ValidationError("Password mismatch")
        return password2
    def save(self,commit=False):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        model=CustomUser
        fields=("email","first_name","last_name","password","is_active","is_admin")

class UserAdmin(BaseUserAdmin):
    form=UserChangeForm
    add_form=UserCreationForm

    list_display=("email","first_name","last_name","is_admin")
    list_filter=("is_admin",)
    fieldsets=(
        (None,{"fields":("email",)}),
        ("Personal Info",{"fields":("first_name","last_name")}),
        ("Permissions",{"fields":("is_admin",)})
    )
    add_fieldsets=(
        (None,{
            "Classes":("wide",),
            "fields":("email","first_name","last_name","password1","password2"),
        }),
    )
    search_fields=("email",)
    ordering=("email",)
    filter_horizontal=()

admin.site.register(CustomUser,UserAdmin)
admin.site.unregister(Group)