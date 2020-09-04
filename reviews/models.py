from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleaniness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        # FK로 타고타고 갈 수도 있음. self.room.name.host 식으로.
        return f"{self.review} - {self.room}"