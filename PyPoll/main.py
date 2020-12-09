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


    #the total number of votes cast
    total_votes = len(voter_id)
    

    #a complete list of candidates who received votes
    #looping through all votes and adding candidates to new list only if not already added 
    candidates = []
    for i in candidate_votes:
            if i not in candidates:
                candidates.append(i)


    #a list of the total number of votes each candidate won
    votes_per_candidate = []
    votes = 0

    #looping through the individual candidates in the candidates list
    #checking how many times their name appears in candidate_votes
    #adding the total number of votes to the new list before moving to the next candidate
    for j in candidates:
        for k in candidate_votes:
            if j == k:
                votes = votes + 1
        next 
        votes_per_candidate.append(votes)
        votes = 0
    next 

    
    #The percentage of votes each candidate won
    #using list comprehension to create a new list 
    #where the values in votes_per_candidate have been converted to percentages
    percentage_votes = ["{:.3%}".format(v/total_votes) for v in votes_per_candidate]
    

    #The winner of the election based on popular vote.   
    #finding the index of the greatest votes
    max_votes = max(votes_per_candidate)
    max_index = votes_per_candidate.index(max_votes)
    winner = candidates[max_index]


    #zip the three lists together to print and export
    #have candidates, votes_per_candidate and percentage_votes
    #all in order with corresponding index's
    votes_summary = zip(candidates, votes_per_candidate, percentage_votes)


    #Printing
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, vote, percent in votes_summary:
        print(f"{candidate}: {percent} ({vote})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")


    #printing to a text file
    #creating a path to the textfile
    output_file = os.path.join('Analysis','PyPoll_result.txt')

    #creating and opening the textfile, then printing the output
    with open(output_file, 'w') as textfile:
    
        textfile.write("Election Results\n")
        textfile.write("-------------------------\n")
        textfile.write(f"Total Votes: {total_votes}\n")
        textfile.write("-------------------------\n")
        votes_summary = zip(candidates, votes_per_candidate, percentage_votes)
        for candidate, vote, percent in votes_summary:
            textfile.write(f"{candidate}: {percent} ({vote})\n")
        textfile.write("-------------------------\n")
        textfile.write(f"Winner: {winner}\n")
        textfile.write("-------------------------\n")
        
       

