from django.shortcuts import render
from .models import Shifts, ShiftSlots
# Create your views here.

def index(request):
    i=[]
    j= []
    user_shifts=  {}
    user_empty_slot = {}
    user_shift_slot = ShiftSlots.objects.filter(userId=request.user.id)
    a= len(user_shift_slot)
    for shift in user_shift_slot:
        user_shift = Shifts.objects.get(id=shift.shiftId_id)
        # print user_shift.capacity
        empty_slot = user_shift.capacity- a
        # print empty_slot
        i.append(user_shift)
        j.append(empty_slot)
    user_shifts.update({'user_shift':i})
    user_empty_slot.update({'empty_slots': j})
    zipped = zip(user_shifts['user_shift'], user_empty_slot['empty_slots'])

    # print (user_shifts,"shfts")
    # print (user_empty_slot, "empty_slots")

    context_dict = {
        'zipped': zipped,

    }
    return render(request, 'home.html', context_dict)