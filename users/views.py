from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from products.models import Article
from .models import Profile
from .models import Profile
from .forms import ProfileForm


@login_required
def profile(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)

    member = Profile.objects.get(user__id=user_id)
    now_user = Profile.objects.get(user__id=request.user.id) 

    like_posts = user.like_articles.all()
    write_posts = user.articles.all() 

    context = {
        "member": member,
        "now_user": now_user,
        "like_posts": like_posts,
        "write_posts": write_posts,
    }
    return render(request, 'users/profile.html', context)

@login_required
def like(request, pk):
    product = get_object_or_404(Article, pk=pk)
    if product.like_users.filter(pk=request.user.pk).exists():
        product.like_users.remove(request.user)

    else:
        product.like_users.add(request.user)

    return redirect("products:product_detail", pk=pk)


def follow(request, user_id):

    if request.user.is_authenticated:
        member = get_object_or_404(Profile, user__id=user_id) 
        now_user = get_object_or_404(Profile, user__id=request.user.id) 

        if member != now_user:
            if now_user in member.followers.all():
                member.followers.remove(now_user)
            else:
                member.followers.add(now_user)
        return redirect("users:profile", member.user.id)
    else:
        return redirect("accounts:login")



def follow(request, user_id):
    if request.user.is_authenticated:
        member = get_object_or_404(Profile, user__id=user_id)
        now_user = get_object_or_404(Profile, user__id=request.user.id)

        if member != now_user:
            if now_user in member.followers.all():
                member.followers.remove(now_user)
            else:
                member.followers.add(now_user)
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