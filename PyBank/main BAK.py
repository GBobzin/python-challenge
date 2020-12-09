import os
import csv

# Path to collect data from the Resources folder#
#budget_csv = os.path.join( "./Resources", "budget_data.csv")
csv_path = "./Resources/budget_data.csv"
#store data as lists
MonthYear =[]
Profitloss= []

#Variables for finding largest and lowest

Max_increase = 0
Min_decrease = 0


# Open file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        # skip the first line as it contains the headers
    next(csvreader, None)
    list_changes = []
    prev= 0
    change = 0
    Max_increase = 0
    Max_increase_date = str()
    Min_decrease = 0
    Min_decrease_date=str()
    
    
    for row in csvreader:
       
        curr = int(row[1])
                
        change = curr - prev

        if change>Max_increase:
            Max_increase = change
            Max_increase_date=row[0]
            list_changes.append(change)
            
        elif change<Min_decrease:
            Min_decrease = change
            Min_decrease_date=row[0]
            list_changes.append(change)

        else:
            list_changes.append(change)

        prev = curr    
                # Add title
        MonthYear.append(row[0])

        # Add profit/Loss
        Profitloss.append(row[1])

# convert values in profitloss into integers for operating
sum_Profitloss = map(int,Profitloss)
#Addition of total operations
Total = sum(sum_Profitloss)

#calculate average change
average_change=round(sum(list_changes[1:])/len(list_changes[1:]),2)

print('Financial Analysis')

print("-----------------------")

#Prints total months by counting items
print(f"Total Months: ",len(MonthYear))
#Prints Total operated
print("Total: $",Total)

print("Average change: $"+ str(average_change))
     
#print(sum(list_changes[1:])/len(list_changes[1:]))
print("Greatest Increase in Profits: "+ str(Max_increase_date) + "  ($"+str(Max_increase)+")" )
print("Greatest Decrease in Profits: "+ str(Min_decrease_date) + "  ($"+str(Min_decrease)+")" )

#printanalysis to text file

f = open('analysis.txt', 'wt')


print('Financial Analysis',file=f)

print("-----------------------",file=f)

#Prints total months by counting items
print(f"Total Months: ",len(MonthYear),file=f)
#Prints Total operated
print("Total: $",Total,file=f)

print("Average change: $"+ str(average_change),file=f)
     
#print(sum(list_changes[1:])/len(list_changes[1:]))
print("Greatest Increase in Profits: "+ str(Max_increase_date) + "  ($"+str(Max_increase)+")",file=f )
print("Greatest Decrease in Profits: "+ str(Min_decrease_date) + "  ($"+str(Min_decrease)+")" ,file=f)

f.close()


