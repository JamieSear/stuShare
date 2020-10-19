from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

    widgets = {
        'Username': forms.TextInput(attrs={'class': 'form-control'}),
        'Comment': forms.Textarea(attrs={'class': 'form-control'}),
    }