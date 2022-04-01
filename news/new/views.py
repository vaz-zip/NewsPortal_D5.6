from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import PostFilter
from .forms import PostForm


class News(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('time_public')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm
        return context


class PostSearch(ListView):
    model = Post
    template_name = '_search.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('time_public')
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'new'


def post_filter(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, '_filtr.html', {'filter': f})


class PostCreateView(CreateView):
    template_name = '_add.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = '_edit.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    context_object_name = 'new'
    queryset = Post.objects.all()
    success_url = '/news/'
