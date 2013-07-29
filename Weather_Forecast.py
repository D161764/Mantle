import urllib2
import re

source=urllib2.urlopen("http://www.accuweather.com/en/in/calcutta/206690/weather-forecast/206690")

text=source.read()
print("<------------------------WEATHER REPORT: KOLKATA--------------------------->")
regex='<strong class="temp">(.+?)<span>(.+?)</span></strong>'
regex1='<span class="cond">(.+?)</span>'
pattern=re.compile(regex)
pattern1=re.compile(regex1)
price=re.findall(pattern,text)
price1=re.findall(pattern1,text)
print "Temperature is: ",price[0][0]," degree celcius"
print "Condition :",price1[0]
