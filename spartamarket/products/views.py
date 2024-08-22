from django.shortcuts import render, redirect
from .forms import CreatedForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .models import Article


def product(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, "products/product.html", context)



@login_required()
# Create your views here.
def create(request):
    if request.method == "POST":
        form = CreatedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:product")

    else:
        form = CreatedForm()
    context = {"form": form}
    return render(request, "products/create.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Article, pk=pk)
    context = { 'product':product}
    return render(request, 'products/product_detail.html', context)




def delete(request, pk):
    product = Article.objects.get(pk=pk)
    product.delete()
    return redirect("products:product")

