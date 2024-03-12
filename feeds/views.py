from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Feed
from .serializers import FeedSerializer

# api/v1/feeds [POST]

class Feeds(APIView):
    # 전체 게시글 데이터 조회
    def get(self, request):
        feeds = Feed.objects.all() # 전체 객체 데이터

        # 객체 -> JSON 형태(시리얼 라이즈)
        serializer = FeedSerializer(feeds, many=True) # 직렬화된 데이터가 담겨있음

        return Response(serializer.data)
    
    def post(self, request):
        # 역직렬화 (클라이언트가 보내준 json -> object)
        serializer = FeedSerializer(data=request.data)

        if serializer.is_valid():
            feed = serializer.save(user=request.user)
            serializer = FeedSerializer(feed)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        except Feed.DoesNotExist:
            raise NotFound
        
    def get(self, request, feed_id): # 클래스 내 함수 self 받아주기
        feed = self.get_object(feed_id) # 클래스 내 자원, 속성, 함수에 접근할 때 self로 접근

        # feed (object) => json => serializer
        serializer = FeedSerializer(feed)
        print(serializer)

        return Response(serializer.data)