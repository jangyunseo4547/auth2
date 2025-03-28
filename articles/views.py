from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
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

@login_required
def detail(request,id):
    article = Article.objects.get(id=id)
    form = CommentForm(request.POST)
    
    context = {
        'article':article,
        'form':form,
    }
    return render(request, 'detail.html', context)

@login_required
def update(request, id):
    article = Article.objects.get(id=id)

    if request.user != article.user:
        return redirect('articles:index')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', id=id)
    
    else:
        form = ArticleForm(instance=article)

    context = {
        'form':form,
    }
    return render(request, 'update.html', context)

@login_required
def delete():
    pass

@login_required
def comment_create(request, article_id): # 댓글은 get 요청으로 들어오는 경우 없음.
    form = CommentForm(request.POST)
    if form.is_valid():                               
        comment = form.save(commit = False)           

        comment.user_id = request.user.id
        comment.article_id = article_id

        # comment.user = request.user                  
        # article = Article.objects.get(id=article_id) 
        # comment.article = article    
        comment.save()                                   

    return redirect('articles:detail',id=article_id)

@login_required
def comment_delete(request, article_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user:
        comment.delete()
    
    return redirect('articles:detail', id=article_id)  
