from django import forms
from .models import Article, Tag


class ArticleCreateForm(forms.ModelForm):

    class Meta:
        model = Article
        # ページに表示したいモデルのフィールドを、文字列で書きます
        fields = '__all__'
        # fields = ('title','text', 'crated_at', 'category', 'tags')

    class TagCreateForm(forms.ModelForm):

        class Meta:
            model = Tag
            fields = '__all__'