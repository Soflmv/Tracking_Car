import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

from django.shortcuts import render
from .models import Info
from django.db.models import Max, Min


def clear(request):
    return render(request, 'car_data/main.html')


def car_data_indb(request):

    global data_all

    try:
        if request.method == 'POST':
            date = request.POST.get('date')
            data_car = request.POST.get('data_car')

            data_all = Info.objects.filter(car_brand=data_car).filter(date=date).order_by('-run')

            max_min_speed = Info.objects.filter(date=date).filter(car_brand=data_car).aggregate(Max('speed'),
                                                                                                Min('speed'))
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
    except TypeError:
        return render(request, 'car_data/main.html')


def pdf_file(request):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4, bottomup=0)
    text_object = c.beginText()
    text_object.setTextOrigin(inch, inch)
    text_object.setFont('Helvetica', 10)

    lines = []

    for i in data_all:
        lines.append(str(i.car_brand))
        lines.append(str(i.driver))
        lines.append(str(i.car_number))
        lines.append(str(i.date))
        lines.append(str(i.speed))
        lines.append(str(i.coordinates))
        lines.append(str(i.run))
        lines.append(str(i.fuel_condition))
        lines.append(str('----------------------'))

    for line in lines:
        text_object.textLine(line)

    c.drawText(text_object)
    c.showPage()
    c.save()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename='data_car.pdf')