import pyowm

owm = pyowm.OWM('456a2d5e8adb346d23b30eae0b602d6f')
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()

print('Wind: '+ str(w.get_wind()))
print('Wind: '+ str(w.get_temperature()))
#w.get_humidity()

