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
    # open_slots= models.IntegerField(null=True, blank=True)
    # @property
    # def open_slot(self):
    #     count_ss= ShiftSlots.objects.filter(shiftId= 6).count()
    #     print (count_ss)
    #     open_slot1= self.shiftId.capacity- count_ss
    #     return open_slot1

    def __unicode__(self):
        return unicode(self.shiftId.id)






