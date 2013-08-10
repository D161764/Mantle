#-------------------------------------------------------------------------------
# Name:        regular backend
# Purpose:
#
# Author:      D1617 64
#
# Created:     11-08-2013
# Copyright:   (c) D1617 64 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sqlite3
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
temperature='<span class="nobr"><span class="b">(.+?)</span>&nbsp;&deg;C</span>'
condition='<div id="curCond">(.+?)</div>'
pattern=re.compile(temperature)
pattern1=re.compile(condition)

# match pattern with htmltext
weather_temp=re.findall(pattern,htmltext)
weather_condition=re.findall(pattern1,htmltext)
print "Temperature is: ",weather_temp[0]," degree celcius"
print "Weather Condition is : ",weather_condition[0]
#for first time used
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect("D://weather_forecast.db")

c = conn.cursor()


# Insert a row of data
c.execute("INSERT INTO wf1 VALUES (?,?)", (weather_temp[0], weather_condition[0]))
# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
