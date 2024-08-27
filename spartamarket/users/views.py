from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model

from products.models import Article
from .models import Profile
from .forms import ProfileForm

# Create your views here.


def profile(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)

    member = Profile.objects.get(user__id=user_id)  # 조화하려는 프로필
    now_user = Profile.objects.get(user__id=request.user.id)  # 현재 로그인한 유저

    like_posts = user.like_articles.all() # 조화하려는 프로필 유저가 좋아요한 게시글
    write_posts = user.articles.all() # 조회하려는 프로필 유저가 작성한 게시글

    context = {
        "member": member,
        "now_user": now_user,
        "like_posts": like_posts,
        "write_posts": write_posts,
    }
    return render(request, 'users/profile.html', context)


def like(request, pk):
    product = get_object_or_404(Article, pk=pk)
    if product.like_users.filter(pk=request.user.pk).exists():
        product.like_users.remove(request.user)
        # product.like_count -= 1
    else:
        product.like_users.add(request.user)
        # product.like_count += 1
    return redirect("products:product_detail", pk=pk)


def follow(request, user_id):
    if request.user.is_authenticated: # 로그인이 되어 있는 경우
        member = get_object_or_404(Profile, user__id=user_id) # 조회할 프로필
        now_user = get_object_or_404(Profile, user__id=request.user.id) # 현재 로그인한 유저의 프로필

        if member != now_user: #현재 로그인한 유저와 조화할 프로필이 같지 않은 경우
            if now_user in member.followers.all(): # 팔로우가 되어있는 경우
                member.followers.remove(now_user) # 팔로우 취소
            else:
                member.followers.add(now_user) # 팔로우하기
        return redirect("users:profile", member.user.id)
    else:
        return redirect("accounts:login")


def update_profile(request, user_id):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, files=request.FILES,
                           instance=user_profile
                           )
        if form.is_valid():
            form.save()
            return redirect("users:profile", user_id)
    else:
        form = ProfileForm(instance=user_profile)
    context = {
        "form": form,
    }

    return render(request, "users/update_profile.html", context)