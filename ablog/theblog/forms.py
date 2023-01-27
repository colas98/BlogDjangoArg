from django import forms
from .models import Post, Category
from datetime import date

# choices =  [('coding', 'coding'), ('essais', 'essais'), ('contes', 'contes'),]
choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'first_post_date', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'ex: This is Title Placeholder stuff'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices = choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'first_post_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder' : 'ex: ' + str(date.today())}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'title_tag', 'body', 'first_post_date', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'This is Title Placeholder stuff'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'first_post_date': forms.DateInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }