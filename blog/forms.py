from django import forms
from blog.models import Post, Comments
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')
        widgets = {'title': forms.TextInput(attrs={'class': 'textinputclass'}), 'text': forms.Textarea(attrs={'class':
                   'editable medium-editor-textarea post-content'})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'text')
        widgets = {'author': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})}


class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        help_texts = {
            'username': None
        }
        widgets = {'password': forms.PasswordInput()}

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Password and Confirm Password does not match.')

