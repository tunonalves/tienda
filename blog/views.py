from django.shortcuts import render, redirect
from blog.models import Post, Categoria
from .forms import formCat,formPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})


def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria':categoria,"posts": posts })


def formpost(request):
    data = {
        'formpost' : formPost()
    }
    if request.method == 'POST':
        forms = formPost(request.POST,request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('Blog')
    else:
        #data['formpost'] = forms
        forms = formPost()
    return render(request,"blog/post.html",{'formpost' : forms})


def formcat(request):
    data = {
        'formcat' : formCat()
    }
    if request.method == 'POST':
        forms = formCat(data=request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('Blog')
    else:
        data['formcat'] = forms
    return render(request,"blog/cats.html",data)


def PostLists(request):
    return render(request,'blog/listPost.html')



class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/listPost.html'

class PostDetalle(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/detailsPost.html'


class PostCreacion(CreateView):
    model = Post
    success_url = reverse_lazy('post_list')#
    fields='__all__'

class PostEdicion(UpdateView):
    model = Post
    success_url = reverse_lazy('post_list')#
    fields='__all__'

class PostEliminacion(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')#
    fields='__all__'