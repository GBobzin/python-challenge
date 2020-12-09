import os
import csv
import statistics

#Stats will be used for the winner calculation
from statistics import mode 

# Path to collect data from the Resources folder#
#budget_csv = os.path.join( "./Resources", "election_data.csv")
csv_path = "./Resources/election_data.csv"


# Open data file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        # skip the first line as it contains the headers
    next(csvreader, None)
    
#variable to count number of total votes, regardless of candidate. Used to calculate %    
    vote_count = 0
    vote_list = []
  
    candidate_list = []

#find candidates by iterating through rows. Also add each ballot to vote_count list.
    for row in csvreader:
        candidate = row[2] 
        ballot = row[2]
        vote_list.append(ballot)
        vote_count = vote_count + 1
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            
    candidate = 0


# Find candidate names
candidate_one = candidate_list[0]
candidate_two = candidate_list[1]
candidate_three = candidate_list[2]
candidate_four = candidate_list[3]
 
# Find number of votes for each candidate
candidate_one_ballots = vote_list.count(candidate_one)
candidate_two_ballots = vote_list.count(candidate_two)
candidate_three_ballots = vote_list.count(candidate_three)
candidate_four_ballots = vote_list.count(candidate_four)



#Print Candidate names, calculate and print % and print total votes

print("Election Results")
print("----------------")
print(f"Total votes: {vote_count}")
print("----------------")
print(f"{candidate_one}: {round(candidate_one_ballots/vote_count*100,3)}% ({candidate_one_ballots})")
print(f"{candidate_two}: {round(candidate_two_ballots/vote_count*100,3)}% ({candidate_two_ballots})")
print(f"{candidate_three}: {round(candidate_three_ballots/vote_count*100,3)}% ({candidate_three_ballots})")
print(f"{candidate_four}: {round(candidate_four_ballots/vote_count*100,3)}% ({candidate_four_ballots})")

#calculate winner, as the mode (most common value) in the vote_list list, containing every single vote.
print("----------------")
print(f'Winner: {mode(vote_list)}')
print("----------------")

#Add script to export as TXT
f = open('analysis.txt', 'wt')


print("Election Results",file=f)
print("----------------",file=f)
print(f"Total votes: {vote_count}",file=f)
print("----------------",file=f)
print(f"{candidate_one}: {round(candidate_one_ballots/vote_count*100,3)}% ({candidate_one_ballots})",file=f)
print(f"{candidate_two}: {round(candidate_two_ballots/vote_count*100,3)}% ({candidate_two_ballots})",file=f)
print(f"{candidate_three}: {round(candidate_three_ballots/vote_count*100,3)}% ({candidate_three_ballots})",file=f)
print(f"{candidate_four}: {round(candidate_four_ballots/vote_count*100,3)}% ({candidate_four_ballots})",file=f)

#calculate winner, as the mode (most common value) in the vote_list list, containing every single vote.
print("----------------",file=f)
print(f'Winner: {mode(vote_list)}',file=f)
print("----------------",file=f)

f.close()