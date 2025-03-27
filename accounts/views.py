from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm


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