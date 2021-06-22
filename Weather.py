import requests
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
h = api_data['main']['humidity']
speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f}°C".format(temp))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",h,'%')
print ("Current wind speed    :",speed,'kmph')

#making a txt file

tlist = [temp, weather_desc, h, speed, date_time]
with open("weather.txt" , mode= 'w', encoding='utf-8') as f:
    f.write("-------------------------------------------------------------\n")
    f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    f.write("\n-------------------------------------------------------------\n")
    f.write("\nCurrent temperature is : {:.2f}°C ".format(tlist[0]))
    f.write("\nCurrent weather desc   : {:s}".format(tlist[1]))
    f.write("\nCurrent Humidity       : {:d}%".format(tlist[2]))
    f.write("\nCurrent wind speed is  : {:.2f}kmph " .format(tlist[3]))
    f.write("\n============================================================")
    f.close()
