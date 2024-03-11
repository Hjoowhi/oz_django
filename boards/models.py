from django.db import models
from common.models import CommonModel

class Board(CommonModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveBigIntegerField(default=0)
    reviews = models.PositiveBigIntegerField(default=0)

    # Board 객체에서 user 데이터 가져오기 -> ForeignKey로 연결해준다.
    # on_delete가 CASCADE이면, user데이터가 삭제되면 board 데이터도 삭제해야 하나? 라는 상황에 둘 다 삭제되는 것이다.
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title