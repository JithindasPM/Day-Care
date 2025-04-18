from django import forms

class Groq_Chat_Form(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control my-1',
            'placeholder': 'Ask anything . . .',
            'style': 'background-color:rgba(255, 255, 255, 0.4); height: 100px;',  # Adjust height
            'rows': 3,  # Set initial rows
        })
    )
    
from django import forms
from .models import Chat

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ["message"]
        
        
from django import forms

class ForgotPasswordForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
