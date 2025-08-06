from django.shortcuts import render
from django.http import HttpResponse
from events.models import Event ,Category, Participant
from django.db.models import Avg, Count
from events.forms import EventModelForm , CategoryModelForm
from django.contrib import messages
from django.shortcuts import redirect

def other(request):
    messages = [1,2,3,4,5,6,7,8,9]
    return render(request, 'test.html', {'messages':messages})

def show_event(request):
    return HttpResponse('<h1>this is our url page</h1>')

def home(request):
    return render(request, 'home.html')

def user(request):
    events = Event.objects.all()
    counts = Event.objects.aggregate(
        total_event = Count('id')
    )
    total_parcipants = Participant.objects.aggregate(total = Count('id'))
    context = {
        'events':events,
        'counts':counts,
        'total_participants':total_parcipants
    }
    return render(request, 'user.html', context)

def admin(request):
    events = Event.objects.all()
    counts = Event.objects.aggregate(
        total_event = Count('id')
    )

    total_parcipants = Participant.objects.aggregate(total = Count('id'))
    context = {
        'events':events,
        'counts':counts,
        'total_participants':total_parcipants
    }
    return render(request, 'admin.html', context)


def create_event(request):
    event_form = EventModelForm()
    category_form = CategoryModelForm()

    if request.method == 'POST':
        event_form = EventModelForm(request.POST)
        category_form = CategoryModelForm(request.POST)
        if event_form.is_valid() and category_form.is_valid():
            category = category_form.save()
            event = event_form.save(commit=False)
            event.category = category
            event.save()
            event_form.save_m2m()

            messages.success(request, message='Task Added Successfully')
            return redirect('create-event')

    context = {
        'event_form':event_form,
        'category_form':category_form
    }

    return render(request, 'form.html', context)


def update_event(request, id):
    event = Event.objects.get(id=id)
    event_form = EventModelForm(instance = event)
    category_form = CategoryModelForm(instance = event.category)
    if request.method == 'POST':
        event_form = EventModelForm(request.POST , instance = event)
        category_form = CategoryModelForm(request.POST , instance = event.category)

        if event_form.is_valid() and category_form.is_valid():
            category = category_form.save()
            event = event_form.save(commit=False)
            event.category = category
            event.save()
            event_form.save_m2m()

            messages.success(request, message='Event Updated Successfully')
            return redirect('create-event')
    context = {
        'event_form':event_form,
        'category_form': category_form
    }

    return render(request, 'form.html', context)


def delete_event(request, id):
    if request.method == 'POST':
        event = Event.objects.get(id = id)
        event.delete()
        messages.success(request, message='Event Deleted Successfully')
        return redirect('admin')
    else:
        messages.error(request, message='Something Went Wrong')
        return redirect('admin')


def event_details(request, id):
    events = Event.objects.filter(id=id).select_related('category').prefetch_related('participants').annotate(total_participants = Count('participants')).first()

    return render(request, 'details.html' , {'events':events})
