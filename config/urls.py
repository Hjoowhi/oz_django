from django.contrib import admin
from django.urls import path, include
# from feeds import views # 기본적인 방법에서 필요 

urlpatterns = [
    path('admin/', admin.site.urls),
    # 공식 문서에서 추천하는 방식
    path('api/v1/feeds/', include('feeds.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/reviews/', include('reviews.urls'))

    # 기본적인 방법
    # url들을 include 시켜주는 경우, 이 path들은 feeds의 urls.py에 간다.
    # path('feeds/', views.show_feed),
    # path('feeds/all', views.all_feed),
    # path('feeds/<int:feed_id>/<str:feed_content>', views.one_feed)
]