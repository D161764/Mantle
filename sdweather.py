import urllib2
import re
import math

city=raw_input('enter city')
str1='hdfForecast?query='
str=str1+city
url = "http://www.wunderground.com/cgi-bin/findweather/%s" % str
source=urllib2.urlopen(url)

htmltext=source.read()





# search for pattern using regular expressions for wundergroung (.+?)
temperature='<span class="nobr"><span class="b">(.+?)</span>&nbsp;&deg;C</span>'
condition='<div id="curCond">(.+?)</div>'
pattern=re.compile(temperature)
pattern1=re.compile(condition)

# match pattern with htmltext for wunderground
weather_temp=re.findall(pattern,htmltext)
weather_condition=re.findall(pattern1,htmltext)

urlbing="http://www.bing.com/search?q=weather+forecast+%s" % city
sourcebing=urllib2.urlopen(urlbing)

htmlbing=sourcebing.read()


# search for pattern using regular expressions for bing (.+?)
tempbing='<div class="w_cur_tb">(.+?)&#176;</div>'
weatherbing='>(.+?)</div><div>&#176;C&nbsp;'
patternbing=re.compile(tempbing)
pattern1bing=re.compile(weatherbing)

# match pattern with htmltext for bing
weather_tempbing=re.findall(patternbing,htmlbing)
weather_conditionbing=re.findall(pattern1bing,htmlbing)

urlask="http://www.ask.com/web?q=weather+forecast+%s" % city
sourceask=urllib2.urlopen(urlask)
htmlask=sourceask.read()

# search for pattern using regular expressions for ask (.+?)
tempask='class="sa_unit_metric"><span class="sa_current_reading">(.+?)&#186'

patternask=re.compile(tempask)
# match pattern with htmltext for ask
weather_tempask=re.findall(patternask,htmlask)


urlch10="http://www.weatherchannel10.com/in/%s" % city
str10='.html'
urlch10=urlch10+str10
sourcech10=urllib2.urlopen(urlch10)
htmlch10=sourcech10.read()
# search for pattern using regular expressions for weatherchannel10 (.+?)
tempch10='/>(.+?)°</div></td><td colspan="2" class="weather">'

patternch10=re.compile(tempch10)

# match pattern with htmltext for weatherchannel10
weather_tempch10=re.findall(patternch10,htmlch10)

 urlwf="http://www.weather-forecast.com/locations/%s" % city
 strwf='/metars/latest'
 urlwf=urlwf+strwf
 sourcewf=urllib2.urlopen(urlwf)
 htmlwf=sourcewf.read()
 # search for pattern using regular expressions for weather-forecast (.+?)
 tempwf='#FF0000;"><span class="temp">(.+?)</span></td>'
 patternwf=re.compile(tempwf)


# match pattern with htmltext for weather-forecast
weather_tempwf=re.findall(patternwf,htmlwf)

a=int(weather_temp[0])
b=int(weather_tempbing[0])
c=int(weather_tempask[0])
d=int(weather_tempch10[0])
e=int(weather_tempwf[0])
mean=a+b+c+d+e

mean=mean/5

a=a-mean
b=b-mean
c=c-mean
d=d-mean
e=e-mean

a=math.pow(a,2)
b=math.pow(b,2)
c=math.pow(c,2)
d=math.pow(d,2)
e=math.pow(e,2)

sd=a+b+c+d+e
sd=sd/5
sd=math.sqrt(sd)







print("<------------------------WEATHER REPORT: "+city.upper()+"--------------------------->")


print "Temperature is (wunder): ",weather_temp[0]," degree celcius"
print "Weather Condition is (wunder) : ",weather_condition[0]

print "Temperature is (bing): ",weather_tempbing[0]," degree celcius"
print "Weather Condition is (bing) : ",weather_conditionbing[0]

print "Temperature is (ask): ",weather_tempask[0]," degree celcius"

print "Temperature is (ch10): ",weather_tempch10[0]," degree celcius"

print "Temperature is (wf): ",weather_tempwf[0]," degree celcius"

print "Temperature in SD form ",sd,"degree celcius"
