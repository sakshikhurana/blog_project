from django import forms
from blog.models import Post, Comments
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')
        widgets = {'title': forms.TextInput(attrs={'class': 'textinputclass'}),
                                                   'text': forms.Textarea(attrs={'class':
                                                                                 'editable medium-editor-textarea'
                                                                                 'post-context'})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'text')
        widgets = {'author': forms.Textarea(attrs={'class': 'editable medoum-editor-textarea'})}


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
