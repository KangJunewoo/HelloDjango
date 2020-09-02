from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.
# 튜플 구성 주의할것! 쉽표 마지막에 안달아주면 그냥 string으로 인식함.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
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
