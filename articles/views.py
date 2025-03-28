from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles':articles,
    }
    return render(request, 'index.html',context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit = False) # 임시 저장 
            article.user = request.user # 유저 정보 가져오기
            article.save() # 저장
            return redirect ('articles:index')

    else:
        form = ArticleForm()

    context = {
        'form':form,
    }
    return render(request, 'create.html', context)
