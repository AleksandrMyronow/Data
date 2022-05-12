##age = int(input ('How old are you?: '));
##if age >= 18:
##    country = str(input('Where are you from? '));
##    if country == 'Ukraine' or country == 'USA' and age >= 18:
##        print('Welcome on board baby');
##    else:
##        print ('You cant watch this content');
##else: 
##    print ('you are too young')

#i = 3;
#while i >= 0:
#    print(i);
#    i=i-1

#import calendar
#print (calendar.month(2022,4))

from pickle import TRUE
from numpy import True_
import pandas as pd
data = pd.read_csv('happyscore_income.csv')
#print(data)

data.sort_values('avg_income', inplace = True)
richest = data[data['avg_income'] > 15000]
print(richest.iloc[0:5])
happy = data['happyScore']
income = data['avg_income']
income.max()
#print(data.columns)

#import matplotlib.pyplot as plt

#plt.scatter(happy, income)
#plt.show()

