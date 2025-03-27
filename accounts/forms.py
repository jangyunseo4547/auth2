from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# signup
class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        #fields = '__all__'
        fields = ('username',) # password도 같이 나옴
        
# login
class CustomAuthenticationForm(AuthenticationForm):
    pass