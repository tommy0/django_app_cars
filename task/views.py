# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import CarCareer, CarModel
import json


def index(request):

    car_model = request.GET.get("car_models")
    if(car_model == "all" or not car_model ):
        car_list = CarCareer.objects.all()
    else:
        car_list = CarCareer.objects.filter(car__model=car_model)

    template = loader.get_template('task/index.html')
    result = []
    for car in car_list:
        result.append(car.to_dict())
    car_model_list = CarModel.objects.all()

    context = {
        'result': result,
        'cars' : car_model_list
    }
    return HttpResponse(template.render(context, request))
