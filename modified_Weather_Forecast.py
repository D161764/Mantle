import urllib2
import re

city=raw_input('enter city')
str1='hdfForecast?query='
str=str1+city
url = "http://www.wunderground.com/cgi-bin/findweather/%s" % str
source=urllib2.urlopen(url)

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
