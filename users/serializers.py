from rest_framework.serializers import ModelSerializer
from .models import User

# 내 정보를 볼 때 추가해줄 시리얼 라이저
class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# 게시글에서 보여줄 유저 데이터
class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'email', 'is_superuser', )