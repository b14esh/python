import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):

    if (request.method == "POST"):
        form = CityForm(request.POST)
        #form.save()
    form = CityForm()

    appid = '08ec16bd0e7f653424e087cdc7b7bfce'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    cities = City.objects.all()

    allcities = []

    for city in cities:

         res = requests.get(url.format(city.name)).json()

         cityinfo = {
              'city': city.name,
              'temp': res["main"]["temp"],
              'icon': res["weather"][0]["icon"]
         }

         allcities.append(cityinfo)

    context = {'all_info': allcities, 'form': form}
    return render(request, 'weather/index.html', context)