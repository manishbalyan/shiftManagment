from django.shortcuts import render
from .models import Shifts, ShiftSlots
# Create your views here.



def index(request):
    i=[]
    user_shifts=  {}
    user_shift_slot = ShiftSlots.objects.filter(userId=request.user.id)
    for shift in user_shift_slot:
        user_shift = Shifts.objects.get(id=shift.shiftId_id)
        i.append(user_shift)
    user_shifts.update({'user_shift':i})




    # print user_shift_slot
    # print user_shifts

    empty_slots = Shifts.objects.all()

    context_dict = {
        'user_shifts': user_shifts

    }
    return render(request, 'home.html', context_dict)