import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join( "Resources", "budget_data.csv")

#store data as lists
MonthYear =[]
Profitloss= []
Month_variation = []

#Variables for finding largest and lowest

Max_increase = 0
Min_decrease = 0


# Open file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        # skip the first line as it contains the headers
    next(csvreader, None)
    for row in csvreader:
        # Add title
        MonthYear.append(row[0])

        # Add profit/Loss
        Profitloss.append(row[1])

#Monthly variance calculation
    






        

# convert values in profitloss into integers for operating
sum_Profitloss = map(int,Profitloss)



#This was to test if info was loading
#print(Profitloss) DELETE THIS!!

#Addition of total operations
Total = sum(sum_Profitloss)

#print(f"{len(Profitloss)+1}")
Max_increase = max(Profitloss)
#Min_decrease = min(Profitloss)



#Prints Total operated
print("total: $",Total)
#Prints total months by counting items
print(f"Total Months: ",len(MonthYear))

print(f"Average change:")

print(f"Greatest Increase in Profits: {Max_increase}") 