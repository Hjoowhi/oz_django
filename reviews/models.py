from django.db import models
from common.models import CommonModel

class Review(CommonModel):
    content = models.CharField(max_length=120)
    likes_num = models.PositiveIntegerField(default=0)

    user = models.ForeignKey('users.User', on_delete=models.CASCADE) # on_delete=models.CASCADE : 삭제될 때 같이 삭제되는지 묻는 것
    feed = models.ForeignKey('feeds.Feed', on_delete=models.CASCADE)