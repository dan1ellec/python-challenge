import os

import csv

#path to collect data from the resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')


#creating lists
date = []
profit = []


#reading using csv module
with open(csvpath) as csvfile:

    #csv reader specifying delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')

    #skipping first heading row in the document
    next(csvreader, None)

    #adding info to date and profit lists
    for row in csvreader:
        
        date.append(row[0])

        profit.append(row[1])


    #the total number of months included in the dataset
    number_of_months = len(date)

    
    #the net total amount of "Profit/Losses" over the entire period
    #adding up everything in the profit/losses column 
    net_amount = 0.00
   
    for x in profit:
        net_amount = net_amount + int(x)
        

    #the average of the changes in "Profit/Losses" over the entire period
    #creating a list to hold the change in profit/loss between each set of months
    changes_list = []

    #adding the difference between each pair of months in the profit list to the changes_list
    for i in range(number_of_months - 1):
        change = int(profit[i + 1]) - int(profit[i])
        changes_list.append(change)

    #adding the values stored in changes_list
    added_changes = 0
    for y in changes_list:
        added_changes = added_changes + int(y)

    #calculating the average
    average_changes = added_changes/(number_of_months - 1)


    #the greatest increase in profits (date and amount) over the entire period
    #finding the greatest profit increase b/w two months, therefore consider changes_list
    #finding the largest increase in profits
    max_number = max(changes_list)

    #finding the index of the largest increase in profits within the list of profit changes
    max_index = changes_list.index(max_number)

    #finding the date for the greatest increase in profits.
    #need to add 1 to the max_index because there is one less data point in changes_list
    max_date = date[max_index + 1]


    #The greatest decrease in losses (date and amount) over the entire period
    #finding the greatest loss b/w two months, therefore consider changes_list
    #finding the smallest increase in profits
    min_number = min(changes_list)

    #finding the index of the smallest increase in profits within the list of profit changes
    min_index = changes_list.index(min_number)

    #finding the date for the greatest decrease in profits.
    #need to add 1 to the max_index because there is one less data point in changes_list
    min_date = date[min_index +1]


    #printing

    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {number_of_months}")
    print(f"Total: {'${}'.format(net_amount)}")
    print(f"Average Change: {'${}'.format(round(average_changes,2))}")
    print(f"Greatest Increase in Profits: {max_date} ({'${}'.format(max_number)})")
    print(f"Greatest Decrease in Profits: {min_date} ({'${}'.format(min_number)})")


    #printing to a text file
    #creating a path to the textfile
    output_file = os.path.join('Analysis','PyBank_result.txt')

    #creating and opening the textfile, then printing the output
    with open(output_file, 'w') as textfile:
    
        textfile.write("Financial Analysis\n")
        textfile.write("--------------------------\n")
        textfile.write(f"Total Months: {number_of_months}\n")
        textfile.write(f"Total: {'${}'.format(net_amount)}\n")
        textfile.write(f"Average Change: {'${}'.format(round(average_changes,2))}\n")
        textfile.write(f"Greatest Increase in Profits: {max_date} ({'${}'.format(max_number)})\n")
        textfile.write(f"Greatest Decrease in Profits: {min_date} ({'${}'.format(min_number)})\n")






#to create a text file
# will need to zip together all the results. so have results in lists??
#then add that zipped thingo to the text file.
#for the below I changed where it said csv in another example to text. 
# not entirely sure if everything I changed is just a variable so will need to check.

#bank_info = zip()

#output_file = os.path.join('financial_result.txt')

#with open(output_file, 'w') as textfile:
    
    #textwriter = text.writer(textfile)
    
    #textwriter.writerows(bank_info)