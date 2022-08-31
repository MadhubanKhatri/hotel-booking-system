from django.db import models

# Create your models here.
class Room(models.Model):
    room_no = models.IntegerField()
    is_booked = models.BooleanField()

    def __str__(self):
        return str(self.room_no)


class Member(models.Model):
    room_no = models.OneToOneField(Room, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=50)
    age = models.IntegerField()
    contact_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    ac_opt = models.CharField(max_length=50)
    bad_opt = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name