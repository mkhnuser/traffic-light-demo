from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(max_length=256, unique=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Forecast(models.Model):
    temperature = models.FloatField(help_text=_("Temperature in Celsius."))
    pressure = models.IntegerField(help_text=_("Atmosphere pressure."))
    wind_speed = models.IntegerField(
        help_text=_("Wind speed in meters per second.")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"For {self.city.name}"
