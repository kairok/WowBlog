from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta

from news.models import  *
from .forms import *
# Create your views here.


#  pip install django-summernote
#  pip install django-allauth

#  admin  kai-65


def news_list(request):
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news":news})


def news_detail(request, pk):
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk, moderration=True)
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect('new_detail', pk)
    else:

        form = CommentForm()
    return render(request, "news/news_detail.html",
                  {"new":new,
                   "comments":comment,
                   "form":form})

def news_filter(request, pk):
    news=News.objects.all()
    if pk == 1:
        now=datetime.now()- timedelta(minutes=60*24*7)
        news=news.filter(created__gte=now)
    elif pk==2:
        now = datetime.now() - timedelta(minutes=60 * 24 * 30)
        news = news.filter(created__gte=now)
    elif pk==3:
        pass

    return render(request, "news/news_list.html", {"news": news})