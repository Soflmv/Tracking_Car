from django.db import models


class Info(models.Model):
    car_brand = models.CharField(max_length=20)
    driver = models.CharField(max_length=30)
    car_number = models.IntegerField()
    date = models.IntegerField()
    speed = models.IntegerField()
    coordinates = models.IntegerField()
    run = models.IntegerField()
    fuel_condition = models.IntegerField()

    def __str__(self):
        return self.car_brand, self.driver, self.car_number, self.date, self.speed, self.coordinates, self.run, \
               self.fuel_condition

