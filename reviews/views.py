from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView

# api/v1/reviews [GET]
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True) # many=True : 여러 개의 객체가 담겨있는 데이터이기 때문

        return Response(serializer.data)

# api/v1/reviews/review_id [GET]
class ReviewDetail(APIView):
    def get(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)
        except:
            raise NotFound
        
        serializer = ReviewSerializer(review)

        return Response(serializer.data)