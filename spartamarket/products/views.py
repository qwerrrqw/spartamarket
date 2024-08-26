from django.db.models import Count

from django.shortcuts import render, redirect
from .forms import CreatedForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Article


def product(request):
    sort = request.GET.get("sort", "")
    if sort == "likes":
        articles = Article.objects.annotate(like_count=Count("like_users")).order_by("-like_count", "-created_at") # 좋아요순 정렬, 동일한 좋아요 순서일 시 최신순으로 정렬
    else:
        articles = Article.objects.all().order_by("-created_at") # 기본 정렬 : 최신순

    # articles = Article.objects.all().order_by("-created_at") # 기본 정렬 : 최신순

    context = {
        "articles": articles,
    }
    return render(request, "products/product.html", context)


@login_required()
# Create your views here.
def create(request):
    if request.method == "POST":
        form = CreatedForm(request.POST, request.FILES)
        print("=========================")
        print(form.is_valid())
        print("=========================")
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("products:product_detail", article.pk)

    else:
        form = CreatedForm()
    context = {"form": form}
    return render(request, "products/create.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Article, pk=pk)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)



@login_required
def delete(request, pk):
    product = Article.objects.get(pk=pk)
    product.delete()
    return redirect("products:product")


@login_required
def edit(request, pk):
    product = get_object_or_404(Article, pk=pk)
    context = {
        "product" : product,
    }
    return render(request, "products/edit.html", context)


def update(request, pk):
    product = get_object_or_404(Article, pk=pk)
    product.title = request.POST.get("title")
    product.content = request.POST.get("content")
    product.save()
    return redirect("products:product_detail", product.pk)