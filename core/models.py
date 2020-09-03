from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    # 저장시간, 생성시간 반영
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # abstract true로 하면 확장용으로, db에 등록되지 않고 코드에서만 쓰임.
        # 인터페이스 같은건가?

        abstract = True