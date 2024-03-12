from rest_framework.serializers import ModelSerializer
from .models import Feed
from users.serializers import FeedUserSerializer
from reviews.serializers import ReviewSerializer

class FeedSerializer(ModelSerializer):
    user = FeedUserSerializer(read_only=True) # ForiegnKey로 연결되어 있다. 유저에 들어가는 데이터를 한번 필터링
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Feed
        fields = '__all__' # Feed라는 model에 있는 전체 fields에 대해 직렬화 하기를 원한다.
        depth = 1