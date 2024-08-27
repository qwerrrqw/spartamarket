from django import forms
from .models import Article


class CreatedForm(forms.ModelForm):
    hashtags = forms.CharField(required=False, help_text="해시태그를 입력해주세요.")
    class Meta:
        model = Article
        fields = "__all__"
        exclude = (
            "author",
            "like_users",
        )

class SearchForm(forms.Form):
    search_word = forms.CharField(label="검색")