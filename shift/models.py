from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Shifts(models.Model):
    day = models.CharField(max_length=10, blank=True, null=True)
    timest = models.TimeField(blank=True, null=True)
    timeend = models.TimeField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    fleetid = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.day

class ShiftSlots(models.Model):
    shiftId = models.ForeignKey(Shifts, default=0, on_delete=models.CASCADE,)
    userId = models.ForeignKey(User, default=0,)

    def __unicode__(self):
        return unicode(self.shiftId.id)






