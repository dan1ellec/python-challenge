import os

import csv

#path to collect data from the resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

# Create individual lists for each column first
# setting variables
voter_id = []
county = []
candidate_votes = []

#reading using csv module
with open(csvpath) as csvfile:

    #csv reader specifying delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')

    #skipping first heading row in the document
    next(csvreader, None)

    #adding info to voter_id, county and candidate_votes
    for row in csvreader:
        
        voter_id.append(row[0])

        county.append(row[1])

        candidate_votes.append(row[2])




    #what we are looking for

    #The total number of votes cast
    #could be caluculated by counting any new list: 3521001

    total_votes = len(voter_id)
    #total_county = len(county)
    #total_candidate = len(candidate_votes)

    #print(f"{total_votes}")
    #print(f"{total_county}")
    #print(f"{total_candidate}")


    #A complete list of candidates who received votes
    #so have to go through candidate votes and note every new person

    candidates = []
    #candidates.append(candidate_votes[0])
    #print(f"{candidates}")

    #for i in range(10):
    #    for j in range(len(candidates)):
    #        if (candidate_votes[i] != candidates[j]):
    #            candidates.append(candidate_votes[i])

    for i in candidate_votes:
            if i not in candidates:
                candidates.append(i)


    #candidates_length = len(candidates)
    #print(f"{candidates_length}")
    print(f"{candidates}")

    #so candidate_votes contains all the votes for the candidates 
    # how many times their name is listed will be how many votes
    #candidates just has the four candidates


    #The total number of votes each candidate won
    
    #candidate_0_count = 0
    
    #for j in candidates:
    #for k in candidate_votes:
    #    if candidates[0] == k:
    #        candidate_0_count = candidate_0_count + 1

    #print(f"{candidate_0_count}")

    #candidate_1_count = 0
    
    #for j in candidates:
    #for k in candidate_votes:
    #    if candidates[1] == k:
    #        candidate_1_count = candidate_1_count + 1

    #print(f"{candidate_1_count}")

    #candidate_2_count = 0
    
    #for j in candidates:
    #for k in candidate_votes:
    #    if candidates[2] == k:
    #        candidate_2_count = candidate_2_count + 1

    #print(f"{candidate_2_count}")

    #candidate_3_count = 0
    
    #for j in candidates:
    #for k in candidate_votes:
    #    if candidates[3] == k:
    #        candidate_3_count = candidate_3_count + 1

    #print(f"{candidate_3_count}")

    #print(candidate_0_count + candidate_1_count + candidate_2_count + candidate_3_count)

    #maybe need to try with a list

    votes_per_candidate = []
    votes = 0

    for j in candidates:
        for k in candidate_votes:
            if j == k:
                votes = votes + 1
        next 
        votes_per_candidate.append(votes)
        votes = 0
    next 

    print(f"{votes_per_candidate}")



    #The percentage of votes each candidate won
    #Feel like it need to find the number first 

    #percentage_votes = [round((v/total_votes)*100, 5) for v in votes_per_candidate]
    #print(f"{percentage_votes}")

    percentage_votes = ["{:.3%}".format(v/total_votes) for v in votes_per_candidate]
    print(f"{percentage_votes}")
    


    #The winner of the election based on popular vote.   


    #will need to zip three lists together to print and export
    # have candidates, votes_per_candidate and percentage_votes
    # all in order with corresponding index's

    votes_summary = zip(candidates, votes_per_candidate, percentage_votes)

    for candidate, vote, percent in votes_summary:
        print(f"{candidate}: {percent} ({vote})")


#Printing
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")