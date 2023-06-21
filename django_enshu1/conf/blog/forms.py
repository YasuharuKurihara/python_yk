from django import forms
from .models import Article, Tag, Comment


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

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class SearchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', required=False)


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        # ページに表示したいモデルのフィールドを、文字列で書きます
        fields = ('name', 'text',) #targetフィールドを含めない