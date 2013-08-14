#-------------------------------------------------------------------------------
# Name: Select operation on backend
# Purpose:
#
# Author: D1617 64
#
# Created: 11-08-2013
# Copyright: (c) D1617 64 2013
# Licence: <your licence>
#-------------------------------------------------------------------------------

import sqlite3
conn=sqlite3.connect("D://weather_forecast.db")
c=conn.cursor()
c.execute('select * FROM wf')
print c.fetchall()
conn.close()
