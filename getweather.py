import pywapi
import os
 
weather_com_result = pywapi.get_weather_from_weather_com('INKL0036')
 
weather = "It is " + weather_com_result['current_conditions']['text'].lower() + " and " + weather_com_result['current_conditions']['temperature'] + " degrees now at your place."
print (weather)
os.system("./ttsspeech.sh "+weather)
