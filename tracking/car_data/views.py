from django.shortcuts import render
from .models import Info
from django.db.models import Max, Min


def clear(request):
    return render(request, 'car_data/main.html')


def car_data_indb(request):
    try:
        if request.method == 'POST':
            date = request.POST.get('date')
            data_car = request.POST.get('data_car')

            data_all = Info.objects.filter(car_brand=data_car).filter(date=date).order_by('-run')

            max_min_speed = Info.objects.filter(date=date).filter(car_brand=data_car).aggregate(Max('speed'), Min('speed'))
            max = max_min_speed.get('speed__max')
            min = max_min_speed.get('speed__min')

            max_min_run = Info.objects.filter(date=date).filter(car_brand=data_car).aggregate(Max('run'), Min('run'))
            max_run = max_min_run.get('run__max')
            min_run = max_min_run.get('run__min')
            all_run = max_run - min_run

            max_min_fuel = Info.objects.filter(date=date).filter(car_brand=data_car).aggregate(Max('fuel_condition'),
                                                                                               Min('fuel_condition'))
            max_fuel = max_min_fuel.get('fuel_condition__max')
            min_fuel = max_min_fuel.get('fuel_condition__min')
            all_fuel = max_fuel - min_fuel

            remainder_fuel = Info.objects.filter(date=date).filter(car_brand=data_car).aggregate(Min('fuel_condition'))
            rem_fuel = remainder_fuel.get('fuel_condition__min')

            return render(request, 'car_data/main.html', {'data_all': data_all, 'max': max, 'min': min,
                                                          'all_run': all_run, 'all_fuel': all_fuel,
                                                          'rem_fuel': rem_fuel})
    except ValueError:
        return render(request, 'car_data/main.html')





