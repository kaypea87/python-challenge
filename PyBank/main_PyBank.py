# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#code for PyBank

#import datafile
import pandas as pd
from pathlib import Path
#path to csv file and read
budget_data = Path("Resources/budget_data.csv")
budget_df = pd.read_csv(budget_data)
budget_df.head()

#The total number of months included in the dataset
monthcount=len(budget_df)
print("Financial Analysis")
print("-------------------")
print(f"Total Months : {monthcount}")
#The net total amount of "Profit/Losses" over the entire period
totalprofit = 0
for i in range(monthcount):
    totalprofit = totalprofit + budget_df["Profit/Losses"][i]


print(f"Total Profit:$ {totalprofit}")
    
    
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#start average at 0
averagesum = 0
monthlychange=[]
for i in range(1,monthcount):
    monthlydiff = budget_df["Profit/Losses"][i]-budget_df["Profit/Losses"][i-1]
    monthlychange.append(monthlydiff)
    averagesum = averagesum + monthlydiff
    
averagechange = averagesum/(monthcount-1)
print(f"Average Change: ${averagechange:.2f}")


#The greatest increase in profits (date and amount) over the entire period
maxvalue = monthlychange[0]
for i in range(1,monthcount-1):
    if maxvalue < monthlychange[i]:
        maxvalue = monthlychange[i]
        maxvaluedate = budget_df["Date"][i+1]
        
print(f"Greatest Increase in Profits: {maxvaluedate} (${maxvalue})")


#The greatest decrease in profits (date and amount) over the entire period
minvalue= monthlychange[0]
for i in range(1,monthcount-1):
    if minvalue > monthlychange[i]:
        minvalue = monthlychange[i]
        minvaluedate = budget_df["Date"][i+1]
        
print(f"Greatest Decrease in Profits: {minvaluedate} (${minvalue})")

#write file to text
file = open('analysis/output.txt','w',encoding ='UTF-8')
file.write("Financial Analysis")
file.write("---------------------")
file.write(f"Total Months : {monthcount}")
file.write(f"Total Profit:$ {totalprofit}")
file.write(f"Average Change: ${averagechange:.2f}")
file.write(f"Greatest Increase in Profits: {maxvaluedate} (${maxvalue})")
file.write(f"Greatest Decrease in Profits: {minvaluedate} (${minvalue})")
file.close()

