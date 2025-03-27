from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST) # 내가 커스텀한 form 불러오기
        if form.is_valid():
            form.save()
            redirect('accounts:login')
        
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form,
    }
    return render(request, 'signup.html',context)

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            redirect('articles:index')

    else:
        form = CustomAuthenticationForm()

    context = {
        'form':form,
    }
    return render(request, 'login.html', context)