from django.shortcuts import redirect, render
from .models import Post, Restaurants

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request, 
        'blog/index.html',
        {
            'posts' : posts
        }
        )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post':post
        }
    )

from django.views.generic import CreateView
from blog.forms import PostForm
from blog.rest_form import RestaurantsForm
# post_new = CreateView.as_view(
#     form_class=PostForm,
#     model=Post,)
#      success_url="/blog/",
# 
def post_new(request):
    # print("request.method=", request.method)
    # print("request.Post=", request.Post)
    if request.method == "GET":
        form=PostForm()
    else:
        form=PostForm(request.POST)
        if form.is_valid():
            #form.cleaned_data
            post = form.save()
            #return redirect(f"/blog/{post.pk}/")
            #return redirect("/blog/")
            return redirect(post)

    return render(request, 'blog/post_form.html', {
        "form": form,
    })

def restaurants(request):
    rest_qs = Restaurants.objects.all().order_by('-pk')

    return render(
        request, 
        'blog/restaurants.html',
        {
            'rest_list': rest_qs,
        }
        )
def resingle_post_page(request, pk):
    rest_qs = Restaurants.objects.get(pk=pk)

    return render(
        request,
        'blog/resingle_post_page.html',
        {
            'rest_qs':rest_qs
        }
    )

def re_new(request):
    # print("request.method=", request.method)
    # print("request.Post=", request.Post)
    if request.method == "GET":
        form=RestaurantsForm()
    else:
        form=RestaurantsForm(request.POST)
        if form.is_valid():
            #form.cleaned_data
            restaurants = form.save()
            #return redirect(f"/blog/{post.pk}/")
            #return redirect("/blog/")
            return redirect(restaurants)

    return render(request, 'blog/rest_form.html', {
        "form": form,
    })
