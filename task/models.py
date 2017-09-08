# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CarModelTypes:
    Belaz = "Белаз"
    Komatsu = "Komatsu"

car_model_choices = ((CarModelTypes.Belaz, "Белаз"),
                     (CarModelTypes.Komatsu, "Komatsu"))


class CarModel(models.Model):
    model = models.CharField(choices=car_model_choices, max_length=100)
    mass = models.IntegerField()


class CarCareer(models.Model):
    car = models.ForeignKey(CarModel)
    number = models.CharField(max_length=10)
    mass = models.IntegerField()
    overload = models.FloatField()

    def to_dict(self):

        return {
            "number": self.number,
            "mass": self.mass,
            "overload": self.overload,
            "mass_max": self.car.mass,
            "model": self.car.model
        }



