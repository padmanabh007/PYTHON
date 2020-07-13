import pandas as pd 
import numpy as np 
from io import StringIO,BytesIO
#dataframe is a combination in the form of rows and columns shows how is your data frame look like
#df=pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'],columns=['C1','C2','C3','C4'])#it is the form of declaration of a dataframe where index is the row name and columns is the column name
#df.to_csv('test1') to create a csv file
#df.loc['Row1'] it will give the valuse in that particular row as series type (indexing)
#df.iloc[:,:] it  work similar to 1 numpy but as data frame if have more than one column(indexing)
#df.iloc[:,:].values      #which will give the values of data in the form of an 2D array
#df.isnull().sum() will return zero in all columns
#df.isnull() will return false in all rows 
#df['C1'].value_counts() it will give how many times a value present in the column 1(for multiple column name put it inside a list)
#df['C1'].unique() shows how many unique values are present in the column 1 

#df=pd.read_csv('auto-mpg.data',us names=['MPG','Cylinders','Displacement','Hourse Power','Weight','Acceleration','Model Year','Orgin'],na_values="?",comment='\t',sep=' ',skipinitialspace= True)#reading a csv file csv=comma seperated values having a sep=,/./;etc will open the file of any type
#where names=coulmnnames use cols ill be giving the columns we wanted to use
#df.head()by default it will be giving top 5 values
#df.info() it will be giving the details about the file
#df.describe() it will give the details about the count,mean,std,min,max,75percentile,25%,50% it will consider only the int and float values and not consider the object features 

#data=('a,b,c,d''\n',
      #'1,2,3,4''\n',
      #'5,6,7,8''\n')
#pd.read_csv(StringIO(data),dtype=object)wher the value of dtype can be of dictionary has index_col parameter which will allow us what to take as the index
#print(data)




#READING JSON
#data={'Employe_name':'Jason','Email':"jasion@gmail.com",'jobprofile':{"title1":"Teamleader",'title2':"Devaloper"}}
#pd.read_json('PATH') it is used to read json format file
#pd.to_jason() #to chnage the value to json
#print(df1)

#reading OF HTML(web scraping)
#pd.read_html('path/url') is used to read an html file matcha is parameter to which the data is to be matched

#Reading the exel file
#pd.read_excel to read the exel file



#PICKLING
#all pandas object are equiped with to_pickle methods which uses python's pickle module to save data str to th e disk in the pickle dta format
# dataname.to_pickle('filename) use to convert to pickle 
#pd.read_pickle('file_name )to read a pickle