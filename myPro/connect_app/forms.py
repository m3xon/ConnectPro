from django import forms
from .models import UserMd

class LoginForm(forms.Form):
    class Meta:
        model = UserMd
        fields =["email", "password",]

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={ 'placeholder': 'Enter your email address'})
        )
    
    password = forms.CharField(
        widget= forms.PasswordInput(attrs = {'placeholder': 'Enter your password' })
    )


class RegistFrom(forms.ModelForm):
    class Meta:
        model = UserMd
        fields = ["full_name", "email", "password", "user_type"]
    
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
        label="Confirm Password"
    )

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={ 'placeholder': 'Enter your fullname'})
        )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={ 'placeholder': 'Enter your email address'})
        )
    
    password = forms.CharField(
        widget= forms.PasswordInput(attrs = {'placeholder': 'Enter your password' })
    )

    user_type = forms.ChoiceField(
        widget=forms.RadioSelect, 
        choices=UserMd.ROLE_CHOICES
    )


    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return password_confirm
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password before saving
        if commit:
            user.save()
        return user