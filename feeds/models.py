from django.db import models
from common.models import CommonModel

# 제목(title), 내용(content), 작성자(User : 객체니깐 대문자)
# Feed와 User의 관계
# 한 명의 유저는 여러 개의 게시글을 작성할 수 있나요? User -> Feed, Feed, Feed (O) 가능
# 하나의 게시글은 여러 유저를 가질 수 있나요? Feed -> User, User, User (X) 설계하기 나름이지만 우린 불가능으로
# User:Feed = 1:N => User(1):feed(N)
class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE) # 유저가 삭제되면 게시글도 삭제