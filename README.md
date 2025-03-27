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