from django.shortcuts import render
from .models import User, Record, Habit
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def habit_tracker(request):
    habits = Habit.objects.all().order_by("created_date")
    return render(request, 'core/tracker.html', {'habits': habits})

def logout(request):
    return render(request, 'accounts/logout/')