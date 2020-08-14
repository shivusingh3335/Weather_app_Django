from django.shortcuts import render
import requests
from .models import City
from . import forms

def index(request):
    cities = City.objects.all() #return all the cities in the database
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=API_KEY' # put your api key in place of API_KEY

    if request.method == 'POST': # only true if form is submitted
        form = forms.CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = forms.CityForm()
    weather_data = []

    for city in cities:

        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list

    context = {'weather_data' : weather_data, 'form': form}
    return render(request, 'weather/index.html',context) #returns the index.html template
    
# 
# 
# city = 'India'
#     city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
#     weather = {
#         'city' : city,
#         'temperature' : city_weather['main']['temp'],
#         'description' : city_weather['weather'][0]['description'],
#         'icon' : city_weather['weather'][0]['icon']
#     }
#     context = {'weather' : weather}
#     return render(request, 'weather/index.html',context) #returns the index.html template
# #url = 'https://api.openweathermap.org/data/2.5/weather?q=India&appid=3968566ea1030f9253089cfb21713b24'