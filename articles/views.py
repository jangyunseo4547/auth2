from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles':articles,
    }
    return render(request, 'index.html',context)

@login_required
def create(request):
     if request.method == 'POST':
         form = ArticleForm(request.POST) # title, content
         if form.is_valid():
             article = form.save(commit=False) # 임시 저장
             article.user = request.user # 로그인한 유저 정보
             article.save()
             return redirect('articles:index')
     else:
         form = ArticleForm()
     
     context = {
         'form':form,
     }
     return render(request, 'create.html', context)
