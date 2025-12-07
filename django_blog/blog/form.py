from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Comment

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email"]

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords do not match")
        return p2



# Adding Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only allow users to enter comment text

    # Optional validation
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 2:
            raise forms.ValidationError("Comment is too short.")
        return content


# blog/forms.py

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3})
        }
