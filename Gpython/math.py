#Is a plotting librry for python programming  and is a numerical mathematical expession Numpy.it provide-
#an oo api for emndedding plots into  application using general purpose toolkit
import matplotlib.pyplot as plt 
import numpy as np 
#x=np.arange(0,10)
#y=np.arange(11,21)
#SCATTER PLOT
#p=plt.scatter(x,y,c='g')#to do the scatter plot represented as a dot
#plt.xlabel('X axis')#to label x axis 
#plt.ylabel('Y axis')#to label y axis
#plt.title('Simple graph') to give the title of graph
#plt.savefig('simple.png') to save the file
#plt.show(p) to shoe the graph


#p=plt.plot(x,y,'r--')# This will be given in the line format straight/curve with colour red and -- indicates doted lines where default colour is blue 

#p=plt.subplot(2,2,1) helps to plot by indexing where index=1 and 2,2 is the number of rows and columns

#Sine And Cosine
#x=np.arange(0,4*np.pi,0.1)#where 0.1 is the sptep size
#y=np.sin(x) to plot a sine wave
#y=np.cos(x) to plot a cosine wave you can use subplot
#p=plt.plot(x,y,'r')
#plt.title('Sine wave')

#BAR plot
#x=[2,8,10]
#y=[11,16,9]
#x2=[3,9,11]
#y2=[6,15,7]
#p=plt.bar(x,y) to get a bar plot of 1st x and y values
#p=plt.bar(x2,y2,color='g') to get the bar plot 2nd x and y value
#plt.title('Bar Graph')
#plt.xlabel('X axis')
#plt.ylabel('Y axis')



#HISTOGRAM
#a=np.array([1,2,3,4,5,6,7,8.5,9])# the values in the x axis on the histogran 
#p=plt.hist(a,bins=20)# by default bins size is 10 and bins will devide the y axis by give density


#Box plot helps to find out percentiles
#a=[np.random.normal(0,std,100) for std in range(1,4)]# it is a list of 3 values where circles are the outliers
#p=plt.boxplot(a,vert=True,patch_artist=True) if patch_artist is false the colour is empty and if vert is false the graph will be represented as thorizontally


#Pie chart
l='Python','C++','Java','Ruby'
s=[215,130,245,210]#these values are based on the cumulative value and assign the values as percentage
c=['Gold','Yellow','Red','blue']
ex=(0.1,0,0,0)#this meanse how nmuch the 1st slice should move
p=plt.pie(s,explode=ex,labels=l,colors=c,autopct='%1.1f%%',shadow=True)#AUTOPCT WILL BE GIVING THE FORMAT in whit the pecentage to be shown shadow indicates different shadows for a slice
plt.show(p)
