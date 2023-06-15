from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Article, Tag


class Home(generic.TemplateView):
    template_name = 'blog/home.html'

class ArticleListView(ListView):
    model =Article
    tempfile_name = 'blog/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

class TagListView(ListView):
    model = Tag
    template_name = 'blog/tag_list.html'
