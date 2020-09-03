from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    pass


class Amenity(AbstractItem):
    pass


class Facility(AbstractItem):
    pass


class HouseRule(AbstractItem):
    pass


class Room(core_models.TimeStampedModel):

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()  # 임포트.. 복뿥할 수고를 덜어줍니다^^
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE
    )  # cascade는 폭포수다. 관련된 모든게 쫘라락 삭제되는 옵션. 보통 이거랑 PROTECT랑 많이 쓰인다.
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
