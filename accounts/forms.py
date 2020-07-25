


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile, interests
from multiselectfield import MultiSelectFormField

class RegistrationForm(UserCreationForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'first_name'}),
        label="First Name")
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'last_name'}),
        label="Last Name")
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'username'}),
        label="Username")
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'email'}),
        label="Email")
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name':'password1'}),
        label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password2'}),
        label="confirm Password")

   #added attributes so as to customise for styling, like bootstrap
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        field_order = ['first_name','last_name','username','email','password1','password2']

    def clean(self):

        """Verifies that the values entered into the password fields match
        NOTE : errors here will appear in 'non_field_errors()'
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please try again!")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    def mail_check(self):
        email = self.cleaned_data('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email already exist")
        return self.cleaned_data

    

    

#The save(commit=False) tells Django to save the new record, but dont commit it to the database yet

class AuthenticationForm(forms.Form): # Note: forms.Form NOT forms.ModelForm

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'username','placeholder':'Username'}),
        label="Username")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
        label='Password')

    class Meta:
        fields = ['username' , 'password']


class EditUserForm(ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'first_name'}),
        label="First Name")
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'last_name'}),
        label="Last Name")
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'username'}),
        label="Username")
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'text','name': 'email'}),
        label="Email")

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

class EditProfileForm(ModelForm):
    
    mobile = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','type':'tel','name': 'mobile'}),
        label="Phone number")
    bio = forms.CharField(widget=forms.Textarea,
        label="Bio")
    birthday = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control','type':'date','name': 'birthday'}),
        label="Username")
    website = forms.URLField(widget=forms.URLInput(
        attrs={'class': 'form-control','type':'url','name': 'website'}),
        label="website")
    gender = forms.ChoiceField(choices=[('M','Male'), ('F','Female'),('O','Other')],
        widget=forms.Select ,
        label="gender")
    

    class Meta:
        model = Profile
        fields = ['mobile','bio','birthday','website','gender']

class interestform(ModelForm):
    
    int_fields = MultiSelectFormField( choices=interests.int_choices )

    class Meta:
        model = interests
        fields = ['int_fields']


    

    