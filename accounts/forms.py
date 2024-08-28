from django.contrib.auth.forms import UserCreationForm,UserChangeForm   
from django.contrib.auth import get_user_model
from django.urls import reverse
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ("email", )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        
        fields = (
            "username",
            "email",
        )

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': '150자 이내로 문자, 숫자, @/./+/- 만 입력 가능합니다.'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control',
                       'placeholder': 'email'}
            )
        }

        label = {
            "username": "ID",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:password_change')}")
            self.fields["password"].help_text = password_help_text
