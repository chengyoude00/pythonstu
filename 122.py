# -*- coding: utf-8 -*-
import urllib2
url='http://aima.cs.berkeley.edu/data/iris.csv'
u=urllib2.urlopen(url)
localfile=open('yy.csv','w')
localfile.write(u.read())
localfile.close()
from numpy import genfromtxt,zeros
data=genfromtxt('yy.csv',delimiter=',',usecols=(0,1,2,3))
target=genfromtxt('yy.csv',delimiter=',',usecols=(4),dtype=str)
print  data.shape
(150,4)
print  target.shape
(150,)
