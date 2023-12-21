from http import HTTPStatus

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.utils.translation import gettext_lazy as _

from .models import City, Forecast
from .utils import (
    collect_information_from_weather_api,
    has_forecast_expired,
    format_forecast_object
)


@require_http_methods(("GET", ))
def get_weather_forecast(request):
    """Gets a weather forecast for a specific city.

    Gets a weather forecast for a specific city. If a request has been made within
    some constant time, returns a local result. Otherwise, makes a request to an API.
    """
    try:
        city = request.GET["city"]
    except KeyError:
        return JsonResponse({
            "__status": "error",
            "__message": _("City query parameter has not been provided."),
        }, status=HTTPStatus.BAD_REQUEST.value)

    try:
        c = City.objects.get(name=city)
    except City.DoesNotExist:
        return collect_information_from_weather_api(city)

    forecast = Forecast.objects.get(city=c)
    if has_forecast_expired(forecast):
        return collect_information_from_weather_api(city)

    return JsonResponse({
        "__status": "success",
        "__message": _("Successfully retrieved information from our local database."),
        **format_forecast_object(forecast)
    })
