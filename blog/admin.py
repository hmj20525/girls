
from django.contrib import admin
from .models import Post

admin.site.register(Post)
#admin에 있는 site라는 register를 불러온 것
#관리자가 포스트를 쓸 수 있도록 하겠다. 라는 의미