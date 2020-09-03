from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# 스무스하게 models.py에서 바꾼 User 등록해주자.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):  # admin 패널에도 변화를 줄 수 있음. 안할거면 pass
    # 기존 필드 + 바나나필드에 새로 정의한 항목들 넣어버리기
    fieldsets = UserAdmin.fieldsets + (
        (
            "Banana",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )


# list_display = ('username', 'email', 'gender', 'language', 'currency', 'superhost')
# list_filter = ('language', 'currency', 'superhost')


# 데코레이터 쓴 건 다음과 같다.
# admin.site.register(models.User, CustomUserAdmin)
