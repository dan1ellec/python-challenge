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
    total_county = len(county)
    total_candidate = len(candidate_votes)

    print(f"{total_votes}")
    print(f"{total_county}")
    print(f"{total_candidate}")


    #A complete list of candidates who received votes
    #so have to go through candidate votes and note every new person


    #The percentage of votes each candidate won


    #The total number of votes each candidate won


    #The winner of the election based on popular vote.   



#Printing
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")