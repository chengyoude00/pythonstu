# -*- coding: utf-8 -*-
import urllib2
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = urllib2.urlopen(url)
localFile = open('iris.csv', 'w')
localFile.write(u.read())
localFile.close()
from numpy import genfromtxt, zeros
# read the first 4 columns
data = genfromtxt('iris.csv',delimiter=',',usecols=(0,1,2,3))
# read the fifth column
target = genfromtxt('iris.csv',delimiter=',',usecols=(4),dtype=str)
print "data:\n ", data
print " target: ", target
print " data.shape: ", data.shape
print " target.shape: ", target.shape
print data.shape



print target.shape
print set(target) # build a collection of unique elements
set(['setosa', 'versicolor', 'virginica'])
from pylab import plot, show
plot(data[target=='setosa',0],data[target=='setosa',2],'bo')
plot(data[target=='versicolor',0],data[target=='versicolor',2],'ro')
plot(data[target=='virginica',0],data[target=='virginica',2],'go')
#show()
from pylab import figure, subplot, hist, xlim, show
xmin = min(data[:,0])
xmax = max(data[:,0])
figure()
subplot(411) # distribution of the setosa class (1st, on the top)
hist(data[target=='setosa',0],color='b',alpha=.7)
xlim(xmin,xmax)
subplot(412) # distribution of the versicolor class (2nd)
hist(data[target=='versicolor',0],color='r',alpha=.7)
xlim(xmin,xmax)
subplot(413) # distribution of the virginica class (3rd)
hist(data[target=='virginica',0],color='g',alpha=.7)
xlim(xmin,xmax)
subplot(414) # global histogram (4th, on the bottom)
hist(data[:,0],color='y',alpha=.7)
xlim(xmin,xmax)
#show()
t = zeros(len(target))
t[target == 'setosa'] = 1
t[target == 'versicolor'] = 2
t[target == 'virginica'] = 3

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(data,t) # training on the iris dataset
#print (classifier.predict(data[0]))

#print (t[0])

from sklearn.model_selection     import  train_test_split  #版本更改由   from sklearn import cross_validation改为from sklearn.model_selection import train_test_split，下面函数的cross_validation删除，直接引用

train, test, t_train, t_test = train_test_split(data, t,test_size=0.4, random_state=0)

classifier.fit(train,t_train) # train
#print classifier.score(test,t_test) # test
#0.93333333333333335

from sklearn.metrics import confusion_matrix
print confusion_matrix(classifier.predict(test),t_test)
#[[16 , 0 , 0],[ 0 ,23 , 3],[ 0 , 0 ,18]]
from sklearn.metrics import classification_report
print classification_report(classifier.predict(test), t_test, target_names=['setosa', 'versicolor', 'virginica'])

from sklearn.model_selection import cross_val_score
# cross validation with 6 iterations
scores = cross_val_score(classifier, data, t, cv=6)
print scores


from numpy import mean
print mean(scores)



from sklearn.cluster import KMeans
kmeans = KMeans(3, init='random') # initialization
kmeans.fit(data) # actual execution

c = kmeans.predict ( data )

from sklearn.metrics import completeness_score, homogeneity_score
print completeness_score(t,c)

print homogeneity_score(t,c)
print set(c)

figure()
subplot(211) # top figure with the real classes
plot(data[t==1,0],data[t==1,2],'bo')
plot(data[t==2,0],data[t==2,2],'ro')
plot(data[t==3,0],data[t==3,2],'go')
subplot(212) # bottom figure with classes assigned automatically
plot(data[c==1,3],data[c==1,2],'bo',alpha=.7)
plot(data[c==2,3],data[c==2,2],'go',alpha=.7)
plot(data[c==0,3],data[c==0,2],'mo',alpha=.7)
show()