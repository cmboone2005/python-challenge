import csv
import os
import numpy as np
from statistics import mean
import sys

stdoutOrigin=sys.stdout
sys.stdout=open("pybanktext.txt","w")


with open("budget_data.csv") as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    next(readCSV)
    dates=[]
    profits_losses=[]
    for row in readCSV:
        date=row[0]
        profit_loss=row[1]

        dates.append(date)
        profits_losses.append(profit_loss)
    #print (dates)
    #print (profits_losses)

print(f"Financial Analysis")
print(f"---------------------------------------")

total_months=len(dates)
print(f"Total Months: {total_months}")

profits_losses = list(map(int, profits_losses))
total_profit=sum(profits_losses)
print(f"Total: ${total_profit}")

changes=np.array(profits_losses)
changes=np.diff(changes)
#print(changes)
average_change = mean(changes)
print(f"Average Change: ${average_change}")

#max_change=max(changes)
#print(max_change)
changes=np.insert(changes,0,0)


find_change=dict(zip(changes,dates))
max_change=max(changes)
max_date=find_change.get(max_change, date)
print(f"Greatest Increase in Profits: {max_date} ({max_change})")
min_change=min(changes)
min_date=find_change.get(min_change, date)
print(f"Greatest Decrease in Profits: {min_date} ({min_change})")

sys.stdout.close()
sys.stdout=stdoutOrigin

print(f"Financial Analysis")
print(f"---------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_date} ({max_change})")
print(f"Greatest Decrease in Profits: {min_date} ({min_change})")


