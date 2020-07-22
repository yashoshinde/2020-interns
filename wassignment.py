
#yashodhan shinde #k.k.wagh college #8857865415 #yashodhanshinde67@gmail.com
import numpy as np  #importing the libraries
import matplotlib.pyplot as plt  #Doing the Task-3
import json
from  datetime import datetime as d

with open('data.json') as w:  #
    data=json.load(w)
with open('latest-rates.json') as y:
    latest_rates=json.load(y)

n= data['rates']  #printing the dataset (data.json)
print (n)
m=latest_rates['rates']   #printing the dataset(latest-rates)
print(m)

fd=d(2019,1,1)
ld=d(2019,1,31)
values=sorted(data['rates'])
INR=list()
GBP=list()
date=list()

for x in values:
  day=d.strptime(x,'%Y-%m-%d')
  if day<=ld and day>=fd:
    INR.append(data['rates'][x]['INR'])
    GBP.append(data['rates'][x]['GBP'])
    date.append([day.day])


plt.plot(date,INR,linewidth=2.0,linestyle='solid',label='INR') #setting up the parameters
plt.plot(date,INR,linewidth=2.0,linestyle='solid',label='GBP')

plt.xlabel('January 2019') #plotting on x-axix
plt.xticks(np.arange(32)) 
plt.ylabel('values with respect to EUR')#plotting on y-axis
plt.title("Plotting the graph of INR and GBP exchange rate against EUR from 1 Jan 2019 to 31 Jan 2019 ")
I=plt.legend(loc="center right") #title for the graph
I.get_texts()[0].set_text("INR="+str(latest_rates['rates']['INR']))
I.get_texts()[1].set_text("GDP="+str(latest_rates['rates']['GDP']))
plt.show()
