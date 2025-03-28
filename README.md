## 공통 html 
- div
    - html의 레이아웃 구성 :`div.container` (들여쓰기) 
    - 동적 데이터를 포함할때
`views.py`
```python
from django.shortcuts import render

def my_view(request):
    context = { # ex) context의 messages
        'username': 'Alice',
        'messages': ['안녕하세요!', 'Django는 재밌어요!', 'Python 최고!']
    }
    return render(request, 'my_template.html', context)
```
`my_template.html`
```shell
<div class="user-info">
    <h2>환영합니다, {{ username }} 님! 🎉</h2>
</div>

<div class="messages">
    {% for msg in messages %}
        <div class="message-box">{{ msg }}</div>
    {% endfor %}
</div>
```

## User modeling 
- `signup 기능 구현`
- AbstractUser : 사용자 인증을 위한 User 모델을 커스텀하고 싶을 때
    - 기본 : username, password
    - 추가 : 추가로 필요한 정보를 커스텀할 수 있음. 

## modeling -> 장고에서 만든 User와 내가 만든 User가 충돌
- `settings.py` : 내가 만든 User 쓰겠다.
```python
AUTH_USER_MODEL = ('accounts.User')
```

`login 기능 구현`
```python 
from django.contrib.auth import login as auth_login 
# 내가 만든 함수 login과 중복되므로 장고 login의 이름을 바꿈.
```

## articles - create 구현 
`views.py`
- method가 POST일떄 ArticleForm 가져오기 
- 유효성 검사 
    - 1) article 변수에 담아 폼을 임시 저장
    - 2) 게시글에 대한 유저 정보 가져오기
    - 3) 게시글 최종 저장
    - 4) 인덱스로 보여주기