from django.urls import path
from . import views

urlpatterns = [
    # config의 urls.py에서 feeds/ 로 설정해주었기 때문에 여기서는 필요 없음
    path('', views.show_feed),
    path('all', views.all_feed),
    path('<int:feed_id>/<str:feed_content>', views.one_feed)
]