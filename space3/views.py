from django.shortcuts import render
from django.views import generic
from blog.models import Post
from django.views.generic import TemplateView
from django.http import HttpResponse


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def about_page(request):
    return render(request, 'about.html')


