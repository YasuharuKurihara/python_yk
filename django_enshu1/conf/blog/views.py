from django.db.models import Q
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from .models import Article, Tag, Comment
from .forms import ArticleCreateForm, TagCreateForm, ArticleUpdateForm, SearchForm, CommentCreateForm
from django.urls import reverse_lazy
from django.shortcuts import redirect


class Home(generic.TemplateView):
    template_name = 'blog/home.html'

class ArticleListView(ListView):
    model =Article
    tempfile_name = 'blog/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context

    def get_queryset(self):
        # 絞り込みのために上書き
        queryset = super().get_queryset()

        # GETパラメータを、フォームに紐づける
        form = SearchForm(self.request.GET)
        form.is_valid()  # フォームからデータを取り出すのに必要な行

        # 値 = フォームオブジェクト.cleaned_data.get('フィールド名')
        keyword = form.cleaned_data.get('keyword')

        if keyword:
            # .filter(フィールド名=値)
            # queryset = queryset.filter(title=keyword)
            # queryset = queryset.filter(title__icontains=keyword)
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset





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

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'blog/comment_create.html'
    success_url = reverse_lazy('blog:home')
    form_class = CommentCreateForm

    def form_valid(self, form):
        comment = form.save(commit=False) #データベースには保存しない
        comment.target = Article.objects.get(pk=self.kwargs['pk'])
        comment.save()
        return redirect('blog:home')