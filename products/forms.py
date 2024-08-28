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

    def __init__(self, *args, **kwargs):
        super(CreatedForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            hashtags = self.instance.hashtags.all()
            initial_hashtags = ' '.join([f"#{hashtag.content}" for hashtag in hashtags])
            self.initial['hashtags'] = initial_hashtags

class SearchForm(forms.Form):
    search_word = forms.CharField(label="검색")

