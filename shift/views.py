from django.shortcuts import render
from .models import Shifts, ShiftSlots
# Create your views here.

def index(request):
    i=[]
    j= []
    ids =[]
    user_shifts=  {}
    user_empty_slot = {}
    user_shift_slot = ShiftSlots.objects.filter(userId=request.user.id)

    for shift in user_shift_slot:
        user_shift = Shifts.objects.get(id=shift.shiftId_id)
        i.append(user_shift)

    for x in i:
        b = ShiftSlots.objects.filter(shiftId = x.id)
        empty_slot = x.capacity - len(b)
        j.append(empty_slot)
        print b
        print empty_slot
    user_shifts.update({'user_shift':i})

    user_empty_slot.update({'empty_slots': j})
    zipped = zip(user_shifts['user_shift'], user_empty_slot['empty_slots'])

    print (user_shifts,"shfts")
    print (user_empty_slot, "empty_slots")

    context_dict = {
        'zipped': zipped,

    }
    return render(request, 'home.html', context_dict)