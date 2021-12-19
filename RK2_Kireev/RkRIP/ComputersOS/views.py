from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from ComputersOS.models import *


def index(request):
    comps = Computer.objects.all()
    os = OS.objects.all()
    return render(request, "index.html", {"comps": comps, "os": os})

def create_comp(request):
    comp = Computer()
    if request.method == "POST":
        comp.name_comp = request.POST.get("name_comp")
        comp.hard_disk_number = request.POST.get("hard_disk_number")
        comp.general_storage = request.POST.get("general_storage")
        comp.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "create_comp.html", {"comp": comp})

def create_os(request):
    comp = Computer.objects.all()
    os = OS()
    if request.method == "POST":
        os.name_os = request.POST.get("name_os")
        os.storage_os = request.POST.get("storage_os")
        os.start_numbers = request.POST.get("start_numbers")
        os.Comp_OS = Computer.objects.get(name_comp=request.POST.get("C_OS"))
        os.save()
        return HttpResponseRedirect("/")
    else:
        return render(request, "create_os.html", {"comp": comp})

# изменение данных в бд
def edit_comp(request, id):
    try:
        comp = Computer.objects.get(id=id)
        if request.method == "POST":
            comp.name_comp = request.POST.get("name_comp")
            comp.hard_disk_number = request.POST.get("hard_disk_number")
            comp.general_storage = request.POST.get("general_storage")
            comp.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_comp.html", {"comp": comp})
    except Computer.DoesNotExist:
        return HttpResponseNotFound("<h2>Компьютер не найден</h2>")

def edit_os(request, id):
    try:
        comp = Computer.objects.all()
        os = OS.objects.get(id=id)
        if request.method == "POST":
            os.name_os = request.POST.get("name_os")
            os.storage_os = request.POST.get("storage_os")
            os.start_numbers = request.POST.get("start_numbers")
            os.Comp_OS = Computer.objects.get(name_comp=request.POST.get("C_OS"))
            os.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit_os.html", {"os": os, "comp": comp})
    except OS.DoesNotExist:
        return HttpResponseNotFound("<h2>ОС не найдена</h2>")

# удаление данных из бд
def delete_comp(request, id):
    try:
        comp = Computer.objects.get(id=id)
        comp.delete()
        return HttpResponseRedirect("/")
    except Computer.DoesNotExist:
        return HttpResponseNotFound("<h2>Компьютер не найден</h2>")

def delete_os(request, id):
    try:
        os = OS.objects.get(id=id)
        os.delete()
        return HttpResponseRedirect("/")
    except OS.DoesNotExist:
        return HttpResponseNotFound("<h2>ОС не найдена</h2>")