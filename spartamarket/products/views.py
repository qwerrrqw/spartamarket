from django.db.models import Count, Q
from django.shortcuts import render, redirect
from .forms import CreatedForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Article, Hashtag


def product(request):
    sort = request.GET.get("sort", "")
    if sort == "likes":
        articles = Article.objects.annotate(like_count=Count("like_users")).order_by("-like_count", "-created_at") # 좋아요순 정렬, 동일한 좋아요 순서일 시 최신순으로 정렬
    else:
        articles = Article.objects.all().order_by("-created_at") # 기본 정렬 : 최신순

    search_form = SearchForm()

    context = {
        "articles": articles,
        "search_form": search_form,
    }

    return render(request, "products/product.html", context)


# Create view
@login_required
def create(request):
    if request.method == "POST":
        form = CreatedForm(request.POST, request.FILES)  # FIlES 추가
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            # 해시태그 파싱 및 저장
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

            # 기존 해시태그를 지우고 새로 추가
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
    search_type = request.GET.get("type")  # 검색 타입 추가

    # 검색 타입에 따라 필터링
    if search_type == 'title':
        article_list = Article.objects.filter(Q(title__icontains=search_word)).distinct()
    elif search_type == 'content':
        article_list = Article.objects.filter(Q(content__icontains=search_word)).distinct()
    elif search_type == 'author':
        article_list = Article.objects.filter(Q(author__username__icontains=search_word)).distinct()
    elif search_type == 'hashtag':  # 해시태그로 검색하는 경우
        article_list = Article.objects.filter(Q(hashtags__content__icontains=search_word)).distinct()
    else:
        # 기본적으로 제목, 내용, 작성자 모두를 검색
        article_list = Article.objects.filter(
            Q(title__icontains=search_word) |
            Q(content__icontains=search_word) |
            Q(author__username__icontains=search_word) |
            Q(hashtags__content__icontains=search_word)  # 해시태그 추가
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
