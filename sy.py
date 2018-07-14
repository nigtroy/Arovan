"""
    :id  => 315202
    :key => 814c59b24b1da8eca1db0b0e28a04c1c
    :url => http://api.openweathermap.org/data/2.5/forecast/city?id=:id&APPID=:key
"""

from urllib.request import urlopen
import json

var url = "https://api.openweathermap.org/data/2.5/weather?q=";

var appid="&appid=456a2d5e8adb346d23b30eae0b602d6f&units=metric"; 

_id = '315202'  # id for Eskisehir
key = '814c59b24b1da8eca1db0b0e28a04c1c'   # api key
url = 'https://api.openweathermap.org/data/2.5/forecast/city?id=' + _id + '&APPID=' + key   # full url

response = urlopen(url).read().decode('utf-8')
obj = json.loads(response)
name = obj['city']['name']
details = []
for state in obj['list']:
    detail = """
    Time : {}
        MAIN
            Temperature : {}
        WIND
            Degree : {}
            Speed  : {}
        WEATHER
            Description : {}
            Main        : {}
""".format(state['dt_txt'][11:16],
           state['main']['temp_kf'],
           state['wind']['deg'],
           state['wind']['speed'],
           state['weather'][0]['description'],
           state['weather'][0]['main'] + "\n" + "-" * 50)
    print(detail)
    details.append(detail)

# save the data to a file
with open('result', 'w') as fp:
    fp.write(str(name).upper() + " WEATHER\n" + "-" * 50 + "\n")
    for detail in details:
        fp.write(detail)
