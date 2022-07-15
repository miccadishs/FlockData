from django.shortcuts import render
from .forms import RecordsForm, VaccinationForm, FlockForm

# Create your views here.
from .models import Farm, Record, Flock, Breed


def dashboard_view(request):
    farms = Farm.objects.all()
    breeds = Breed.objects.all()

    unique_farms = set(farms)
    # farm_records = {}
    # for farm in unique_farms:
    #     records = Record.objects.filter(flock__house__site__farm__name=farm.name)
    #     farm_records[farm.name] = records

    farm_flocks = {}
    farm_flocks_list = []
    farm_name = []

    for farm in unique_farms:
        flocks = Flock.objects.filter(house__site__farm__name=farm.name)
        farm_flocks[farm.name] = flocks
        farm_flocks_list.append({farm.name: flocks})
        farm_name.append(farm.name)

    context = {
        'breeds': breeds
    }
    return render(request, 'flocks/dashboard.html', context)


def flocks_list(request, farm):
    flocks = Flock.objects.filter(house__site__farm__name=farm)
    context = {
        'flocks': flocks
    }
    return render(request, 'flocks/flocks-list.html', context)


def records_view(request):
    form = RecordsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }

    return render(request, 'flocks/records.html', context)


def vaccinations_view(request):
    form = VaccinationForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'flocks/vaccinations.html', context)


def flocks_view(request):
    form = FlockForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'flocks/flocks.html', context)


def owners_view(request):
    return render(request, 'flocks/owners.html')


def houses_view(request):
    return render(request, 'flocks/houses.html')


def farms_view(request):
    return render(request, 'flocks/farms.html')


def settings_view(request):
    return render(request, 'flocks/settings.html')
