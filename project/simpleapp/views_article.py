from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import ArticleFilter
from .forms import ArticleForm
from .models import Article


class ArticlesList(ListView):
    model = Article
    ordering = 'title'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticleFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class ArticleCreate(CreateView):
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'


class ArticleUpdate(UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'
    pk_url_kwarg = 'id'


class ArticleDelete(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    pk_url_kwarg = 'id'


class ArticleSearch(ListView):
    model = Article
    template_name = 'article_search.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticleFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
