from django.db.models import Count, Q
from django.shortcuts import render, redirect
from .forms import CreatedForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Article, Hashtag


def product(request):
    sort = request.GET.get("sort", "")
    if sort == "likes":
        articles = Article.objects.annotate(like_count=Count("like_users")).order_by("-like_count", "-created_at")
    else:
        articles = Article.objects.all().order_by("-created_at")

    search_form = SearchForm()

    context = {
        "articles": articles,
        "search_form": search_form,
    }

    return render(request, "products/product.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = CreatedForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            hashtags_input = form.cleaned_data.get('hashtags', '')
            hashtags = set(word for word in hashtags_input.split() if word.startswith('#'))
            for hashtag in hashtags:
                cleaned_hashtag = hashtag.strip("#")
                if cleaned_hashtag:
                    hashtag_obj, created = Hashtag.objects.get_or_create(content=cleaned_hashtag)
                    article.hashtags.add(hashtag_obj)
            article.save()
            return redirect("products:product_detail", article.pk)
    else:
        form = CreatedForm()
    context = {"form": form}
    return render(request, "products/create.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Article, pk=pk)
    hashtags = product.hashtags.all() 
    context = { 
            'product': product,
            'hashtags': hashtags,
            }

    return render(request, 'products/product_detail.html', context)


@login_required
def delete(request, pk):
    product = Article.objects.get(pk=pk)
    product.delete()
    return redirect("products:product")


@login_required
def update(request, pk):
    product = get_object_or_404(Article, pk=pk)
    
    if request.method == "POST":
        form = CreatedForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            article.hashtags.clear()
            hashtags_input = form.cleaned_data.get('hashtags', '')
            hashtags = set(word for word in hashtags_input.split() if word.startswith('#'))
            for hashtag in hashtags:
                cleaned_hashtag = hashtag.strip("#")
                if cleaned_hashtag:
                    hashtag_obj, created = Hashtag.objects.get_or_create(content=cleaned_hashtag)
                    article.hashtags.add(hashtag_obj)
                    
            return redirect("products:product_detail", article.pk)
    else:
        form = CreatedForm(instance=product)
    context = {"form": form, "product": product}
    return render(request, "products/update.html", context)



def search(request):
    search_word = request.GET.get("search_word")
    search_type = request.GET.get("type")
    if search_type == 'title':
        article_list = Article.objects.filter(Q(title__icontains=search_word)).distinct()
    elif search_type == 'content':
        article_list = Article.objects.filter(Q(content__icontains=search_word)).distinct()
    elif search_type == 'author':
        article_list = Article.objects.filter(Q(author__username__icontains=search_word)).distinct()
    elif search_type == 'hashtag':
        article_list = Article.objects.filter(Q(hashtags__content__icontains=search_word)).distinct()
    else:
        article_list = Article.objects.filter(
            Q(title__icontains=search_word) |
            Q(content__icontains=search_word) |
            Q(author__username__icontains=search_word) |
            Q(hashtags__content__icontains=search_word)
        ).distinct()

    context = {
        "search_word": search_word,
        "article_list": article_list,
    }

    return render(request, "products/search.html", context)


@login_required
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    products = Article.objects.filter(hashtags=hashtag).order_by('-pk')
    context = {
        "hashtag": hashtag,
        "products": products,
    }
    return render(request, 'products/hashtag.html', context)
