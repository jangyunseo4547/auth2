from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm):
    class Meta():
        model = Article
        # fields = '__all__'
        exclude = ('user',)

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ('content',)


