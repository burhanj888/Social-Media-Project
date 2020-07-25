from django import forms
from .models import Post


class HomeForm(forms.ModelForm):
    caption = forms.CharField(required=False,widget=forms.Textarea(
        attrs={
            'class': 'form-control no-border',
            'placeholder': 'Write your views...',
        }
    ))

    image = forms.FileField(required=False ,widget=forms.FileInput(
        attrs={
            'class': 'form-control',
            'type': 'file',

        }
    ))
    

    class Meta:
        model = Post
        fields = ('image','caption', 'category')