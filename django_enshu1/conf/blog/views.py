from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from .models import Article, Tag
from .forms import ArticleCreateForm, TagCreateForm, ArticleUpdateForm
from django.urls import reverse_lazy


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


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = ArticleCreateForm

class TagCreateView(CreateView):
    model = Tag
    template_name = 'blog/tag_create.html'
    success_url = reverse_lazy('blog:tag_list')
    form_class = TagCreateForm

class ArticleUpdateView(generic.UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'blog/article_update.html'
    success_url = reverse_lazy('blog:article_list')

class ArticleDeleteView(generic.DeleteView):
    model = Article
    template_name = 'blog/article_delete.html'
    success_url = reverse_lazy('blog:article_list')