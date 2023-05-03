#list modules used for script

import csv
import os 

#declare variables for script
totalmonths = 0
nettotal = 0
totalprofit = 0
prevprofit = 0
profitchange = 0
greatestincrease = 0
greatestdecrease = 10000
increasedate = ''
decreasedate = ''
totalprofitlist = []


#csvpath to access file
csvpath = os.path.join('PyBank/Resources/budget_data.csv')


#open csv file that will be analyzed
with open(csvpath) as csvfile:


#read csv file
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)

#skip first row header

    csvheader = next(csvreader)
    firstrow = next(csvreader)
    totalmonths = 1
    firstprofit = int(firstrow[1])
    totalprofit = int(firstrow[1])

#loop through all rows in data & calculate average change
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
        totalmonths += 1 
        totalprofit += profit


        nettotal = profit - firstprofit
        totalprofitlist += [nettotal]
        firstprofit = profit

        if nettotal > greatestincrease:
            greatestincrease = nettotal
            increasedate = date

        if nettotal < greatestdecrease:
            greatestdecrease = nettotal
            decreasedate = date


    #average profit change formula
    averagechange = sum(totalprofitlist) / len(totalprofitlist)

        
#output of results

output = f"""
Financial Analysis
----------------------------
Total Months: {totalmonths}
Total: ${totalprofit}
Average Change: ${averagechange}
Greatest Increase in Profits: {increasedate} (${greatestincrease})
Greatest Decrease in Profits: {decreasedate} (${greatestdecrease})
"""

print(output)
#path for text file
textpath = os.path.join('PyBank/Analysis/Pybank Text File.txt')

with open(textpath,'w') as csvfile:
    csvfile.write(output)
