from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'first_post_date')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ex: This is Title Placeholder stuff'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'first_post_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder' : 'ex: 2022-01-30'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'first_post_date')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'This is Title Placeholder stuff'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'first_post_date': forms.DateInput(attrs={'class': 'form-control'})
        }