from django import forms
from .models import Article

class CreatedForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        # exclude = ()
