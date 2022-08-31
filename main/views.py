from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse
from .models import Room, Member

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})


def room_booking(request, room_no):
    return render(request, 'room_booking.html', {'room_no': room_no})


def booking_confirm(request, room_num):
    full_name = request.POST['fname']
    age = request.POST['age']
    contact_num = request.POST['contact_no']
    gender = request.POST['gender']
    bad_option = request.POST['bad']
    ac_option = request.POST['ac']

    if not full_name or not age or not contact_num or not bad_option or not ac_option:
        return HttpResponse('Please enter data in the fields')
    else:
        room_status = Room.objects.get(room_no=room_num)
        room_status.is_booked = True

        member = Member.objects.create(room_no=room_status, full_name=full_name, age=age,
         contact_number=contact_num, gender=gender, bad_opt = bad_option, ac_opt = ac_option)
        member.save()
        room_status.save()
        return redirect('home')
    
    
