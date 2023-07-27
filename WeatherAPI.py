import requests
import json
response=requests.request("GET","https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
data=response.json()
dates=[]
pressure=[]
wind_speed=[]
temperature=[]
for i in range(0,len(data["list"])-1):
    dates.append(str(data["list"][i]['dt_txt']))
    pressure.append(str(data["list"][i]["main"]["pressure"]))
    wind_speed.append(str(data["list"][i]["wind"]["speed"]))
    temperature.append(str(data["list"][i]["main"]["temp"]))
print("Please enter \n1 to get the weather \n2 to get the wind speed\n3 to get the pressure\n0 to exit")
n=int(input())
if(n==0):
    print()
else:
    date=str(input("Date and time should be given as yyyy-mm-dd hh:mm:ss :::"))
    while(n>0):
        if(
                date in dates):
            val=dates.index(date)
            if(n==1):
                print("1. temp of the input date ",date,"is ",temperature[val])
            elif(n==2):
                print("2. Wind Speed of the input date ",date,"is ",wind_speed[val])
            elif(n==3):
                print("3. Pressure of the input date ",date,"is ",pressure[val])
        else:
            print("Please enter the valid date or time")
        n=int(input())
        if(n!=0):
            date=str(input("Date and time should be given as yyyy-mm-dd hh:mm:ss :::"))