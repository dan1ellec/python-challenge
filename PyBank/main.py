import os

import csv

#path to collect data from the resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

#reading using csv module
with open(csvpath) as csvfile:

    #csv reader specifying delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')




#The total number of months included in the dataset
#counting through the number of rows???

#The net total amount of "Profit/Losses" over the entire period
#this would be adding up everything in the profit/losses column to see what the net profit or loss was

#The average of the changes in "Profit/Losses" over the entire period
#this would be net total / number of months

#The greatest increase in profits (date and amount) over the entire period
# somehow finding biggest number in profits/losses column and identifying the date


#The greatest decrease in losses (date and amount) over the entire period
# # somehow finding smallest number in profits/losses column and identifying the date


# want to both print report to the terminal and create text file with the results.


#to create a text file
# will need to zip together all the results. so have results in lists??
#then add that zipped thingo to the text file.
#for the below I changed where it said csv in another example to text. 
# not entirely sure if everything I changed is just a variable so will need to check.

bank_info = zip()

output_file = os.path.join('financial_result.txt')

with open(output_file, 'w') as textfile:
    
    textwriter = text.writer(textfile)
    
    textwriter.writerows(bank_info)