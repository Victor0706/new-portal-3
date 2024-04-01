from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import NewFilter
from .forms import NewForm
from .models import New


class NewsList(ListView):
    model = New
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewDetail(DetailView):
    model = New
    template_name = 'new.html'
    context_object_name = 'new'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context

class NewCreate(CreateView):
    form_class = NewForm
    model = New
    template_name = 'new_edit.html'


class NewUpdate(UpdateView):
    form_class = NewForm
    model = New
    template_name = 'new_edit.html'
    pk_url_kwarg = 'id'


class NewDelete(DeleteView):
    model = New
    template_name = 'new_delete.html'
    success_url = reverse_lazy('new_list')
    pk_url_kwarg = 'id'


class NewSearch(ListView):
    model = New
    template_name = 'new_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


