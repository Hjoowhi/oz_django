from django.db import models

# Create your models here.
class CommonModel(models.Model):
    # auto_now_add : 현재 데이터 생성 시간을 기준으로 생성된다. -> 이후 데이터가 업데이트 되어도 수정되지 않는다.
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now : 생성되는 시간 기준으로 일단 생성된다. -> 이후 데이터가 업데이트 되면 시간도 업데이트된 현재 시간을 기준으로 업데이트 된다.
    updated_at = models.DateTimeField(auto_now=True)

    # 테이블에 관련된 옵션 설정
    # 두 개의 컬럼을 만들었을 때, 우리가 만든 DB에 추가가 되지 않도록 한다. -> 전체에서 공통으로 사용하기 때문
    class Meta:
        abstract = True # 데이터베이스의 데이블에 위와 같은 컬럼이 추가되지 않는다.