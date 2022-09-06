from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    firstname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}))
        


    lastname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'}))


    email = forms.EmailField(
        required=True ,
        widget=forms.EmailInput(attrs={'autocomplete': 'new-password' , 'class':'form-control'}))

    phonenumber = forms.CharField(
        required=True,
        max_length=11 , 
        widget=forms.TextInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(
        min_length= 10 ,
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control'}),

    )
    password2 = forms.CharField(
        min_length= 10 ,
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )


    class Meta:
        model = CustomUser
        fields = ['firstname' ,'lastname' , 'email', 'phonenumber','password1' , 'password2']

    
    def clean_phonenumber(self):
        phonenumber = self.cleaned_data["phonenumber"]
        if CustomUser.objects.filter(phone_number=phonenumber).exists():
            raise forms.ValidationError("Phone already exists")
        return phonenumber

    def clean_email(self):
        email = self.cleaned_data["email"]
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Address already exists")
        return email

    def clean_password2(self):
        password2 = self.cleaned_data.get("password2")
        password1 = self.cleaned_data.get("password1")
        if password2 != password1 :
            raise forms.ValidationError("password is not match")
        return password1


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user


    


    
 
        
    

        







class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email']












class MyUserLoginForm(forms.Form):

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'autocomplete': 'new-password' , 'class':'form-control'}))


    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password' , 'class':'form-control'})) 




    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        user = authenticate(email=email, password=password)

        if user is None:
            raise forms.ValidationError("Email or password incorrect")

        if not user.check_password(password):
            raise forms.ValidationError(" password incorrect")
        
        if not user.is_active :
            raise forms.ValidationError("Email or password incorrect please ")

        return user 