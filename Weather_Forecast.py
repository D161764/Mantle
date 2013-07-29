import urllib2
import re

city=raw_input("Enter City:")

# Vary Sources as per city

if(city=="Kolkata" or city=="kolkata" or city=="KOLKATA"):
    source=urllib2.urlopen("http://www.accuweather.com/en/in/calcutta/206690/weather-forecast/206690")
elif(city=="Bangalore" or city=="bangalore"):
    source=urllib2.urlopen("http://www.accuweather.com/en/in/bangalore/204108/weather-forecast/204108")
elif(city=="Delhi"):
    source=urllib2.urlopen("http://www.accuweather.com/en/in/delhi/202396/weather-forecast/202396")
elif(city=="Chennai"):
    source=urllib2.urlopen("http://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671")

else:
    print "City not in Database.Choose a different one."


# Web Scraping using urllib2

htmltext=source.read()
print("<------------------------WEATHER REPORT: "+city.upper()+"--------------------------->")

# search for pattern using regular expressions (.+?)
temperature='<strong class="temp">(.+?)<span>(.+?)</span></strong>'
condition='<span class="cond">(.+?)</span>'
pattern=re.compile(temperature)
pattern1=re.compile(condition)

# match pattern with htmltext
weather_temp=re.findall(pattern,htmltext)
weather_condition=re.findall(pattern1,htmltext)
print "Temperature is: ",weather_temp[0][0]," degree celcius"
print "Condition :",weather_condition[0]
