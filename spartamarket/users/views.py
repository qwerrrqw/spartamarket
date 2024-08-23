from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from products.models import Article
from .models import Profile

# Create your views here.


def profile(request, user_id):
    user = request.user # 로그인된 사용자
    member = get_object_or_404(get_user_model(), id=user_id) #my_user를 member로 변경, 프로필 주인
    products = member.like_articles.all() # member로 변경
    profile_user = get_object_or_404(Profile, user_id=user_id)
    followers_count = profile_user.followers.count()
    context = {
        "user": user, #my_user를 user로 변경
        "products": products,
        "member": member, # "member": member 추가
        'profile_user': profile_user,
        "followers_count": followers_count,
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
    member = get_object_or_404(Profile, user__id=user_id)  # Profile 모델과 user__id로 필터링하여 객체 가져오기
    user_profile = request.user.profile  # 로그인된 사용자의 프로필을 가져오기

    if user_profile in member.followers.all():
        member.followers.remove(user_profile)
    else:
        member.followers.add(user_profile)
    
    return redirect('users:profile', user_id=user_id)