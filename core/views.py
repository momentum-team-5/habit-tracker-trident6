from django.shortcuts import render, get_object_or_404, redirect
from core.models import Habit, Record
from core.forms import HabitForm, RecordForm

def welcome(request):
    return render(request, "core/habit_welcome.html")

def habit_list(request):
    habits = request.user.habits.all()
    return render(request, "core/habit_list.html", {"habits": habits})

def habit_detail(request, pk):
    habit = get_object_or_404(Habit, id=pk)
    return render(request, "core/habit_detail.html", {"habit": habit})

def habit_create(request):
    if request.method == "GET":
        form = HabitForm()
    else:
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            # check ckeck author or user
            habit.user = request.user 
            habit.save()
            return redirect(to="habit_list")
    return render(request, "core/habit_create.html", {"form": form})   


def habit_update(request, pk):
    habit = get_object_or_404(request.user.habits.all(), pk=pk)

    if request.method == "GET":
        form = HabitForm(instance=habit)
    else:
        form = HabitForm(data=request.POST, instance=habit)

        if form.is_valid():
            form.save()

            return redirect(to="habit_list")

        else:
            #error(request, "Your updates didn't work :(")
            pass

    return render(request, "core/habit_update.html", {"form": form})

def habit_delete(request, pk):
    habit = get_object_or_404(request.user.habits.all(), pk=pk)
    habit.delete()
    #success message

    return redirect(to="habit_list")

# Record section

def record_list(request):
    user = request.user
    records = user.record.all()
    form = RecordForm()
    return render(request, "core/record_list.html", {"records": records, "form": form})

# def record_list(request):
#     records = request.user.records.all()
#     return render(request, "core/record_list.html", {"records": records})






def record_detail(request, pk):
    record = get_object_or_404(Record, id=pk)
    return render(request, "core/record_detail.html", {"record": record})

def record_create(request):
    if request.method == "GET":
        form = RecordForm()
    else:
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            # check ckeck author or user
            record.user = request.user 
            record.save()
            return redirect(to="record_list")
    return render(request, "core/record_create.html", {"form": form})   



# habit_list - habits/, root path ("")
# habit_detail - habits/<int:pk>/
# habit_create - habits/create/
# habit_update - habits/<int:pk>/update/
# habit_delete - habits/<int:pk>/delete/
# record_create - habits/<int:habit_pk>/create-record/
# record_update - records/<int:pk>/update/
# record_delete - records/<int:pk>/delete/