from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model

from products.models import Article
from .models import Profile

# Create your views here.


def profile(request, user_id):
    user = request.user
    # products = user.like_users.filter(user_id=user)

    my_user = get_object_or_404(get_user_model(), id=user_id)
    products = my_user.like_articles.all()

    context = {
        "user": my_user,
        "products": products,
    }
    return render(request, 'users/profile.html', context)


def like(request, pk):
    product = get_object_or_404(Article, pk=pk)
    if product.like_users.filter(pk=request.user.pk).exists():
        product.like_users.remove(request.user)
        print("like_false")
    else:
        product.like_users.add(request.user)
        print("like_true")
    return redirect("products:product_detail", pk=pk)


def follow(request, user_id):
    member = get_user_model().objects.get(id=user_id)
    print(member)
    print(dir(member))
    print(member.profile)
    if  member.followers.filter(pk=request.user.pk).exists():
        member.followers.remove(request.user)
    else:
        member.followers.add(request.user)
    return redirect('users:profile', member.username)
