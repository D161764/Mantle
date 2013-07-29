import urllib2
import re

city=raw_input("Enter City:")

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




text=source.read()
print("<------------------------WEATHER REPORT: "+city.upper()+"--------------------------->")
regex='<strong class="temp">(.+?)<span>(.+?)</span></strong>'
regex1='<span class="cond">(.+?)</span>'
pattern=re.compile(regex)
pattern1=re.compile(regex1)
price=re.findall(pattern,text)
price1=re.findall(pattern1,text)
print "Temperature is: ",price[0][0]," degree celcius"
print "Condition :",price1[0]
