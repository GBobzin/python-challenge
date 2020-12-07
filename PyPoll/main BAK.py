import os
import csv

# Path to collect data from the Resources folder#
#budget_csv = os.path.join( "./Resources", "election_data.csv")
csv_path = "./Resources/election_data.csv"


# Open file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        # skip the first line as it contains the headers
    next(csvreader, None)
    
    vote_count = 0
    vote_list = []
  
    candidate_list = []
#find candidates
    for row in csvreader:
        candidate = row[2] 
        ballot = row[2]
        vote_list.append(ballot)
        vote_count = vote_count + 1
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            
    candidate = 0

#Work out election results


# Find candidate names
candidate_one = candidate_list[0]
candidate_two = candidate_list[1]
candidate_three = candidate_list[2]
candidate_four = candidate_list[3]
 
# Find votes for each candidate
candidate_one_ballots = vote_list.count(candidate_one)
candidate_two_ballots = vote_list.count(candidate_two)
candidate_three_ballots = vote_list.count(candidate_three)
candidate_four_ballots = vote_list.count(candidate_four)




print(f"{candidate_one}: {round(candidate_one_ballots/vote_count*100,3)}% ({candidate_one_ballots})")
print(f"{candidate_two}: {round(candidate_two_ballots/vote_count*100,3)}% ({candidate_two_ballots})")
print(f"{candidate_three}: {round(candidate_three_ballots/vote_count*100,3)}% ({candidate_three_ballots})")
print(f"{candidate_four}: {round(candidate_four_ballots/vote_count*100,3)}% ({candidate_four_ballots})")

'''
print(f"{candidate_two} : received {candidate_two_ballots}")   
print(f"{candidate_three} : received {candidate_three_ballots}") 
print(f"{candidate_four} : received {candidate_four_ballots}")       
 '''   


#print outcomes
'''
print("Total Votes: " +  str(vote_count))
print(str(candidate_one))
print(str(candidate_two))
print(str(candidate_three))
print(str(candidate_four))
'''