from django.contrib.auth.forms import UserCreationForm,UserChangeForm   
from django.contrib.auth import get_user_model
from django.urls import reverse


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password_help_text = (
                "You can change the password " '<a href="{}">here</a>.'
            ).format(f"{reverse('accounts:password_change')}") #format 뒤에 값이 href 뒤 {}에 들어간다 
            self.fields["password"].help_text = password_help_text