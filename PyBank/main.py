import os

import csv



#path to collect data from the resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')


#creating some variables

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


    #The total number of months included in the dataset
    #counting through the number of rows???

    number_of_months = len(date)

    
    #The net total amount of "Profit/Losses" over the entire period
    #this would be adding up everything in the profit/losses column to see what the net profit or loss was
    net_amount = 0.00
   
    for x in profit:
        net_amount = net_amount + int(x)
        

    #The average of the changes in "Profit/Losses" over the entire period
    #this would be net total / number of months
    #average = net_amount/number_of_months
    #that isn't right! it is some other formula

    #i think this will give the value of y - 1 not the position y -1
    #changes = 0
    #for y in profit:
       # changes = changes + (int(row{y+1) - int(y)
    
    changes_list = []

    for i in range(number_of_months - 1):
        change = int(profit[i + 1]) - int(profit[i])
        changes_list.append(change)

    added_changes = 0
    for y in changes_list:
        added_changes = added_changes + int(y)

    average_changes = added_changes/(number_of_months - 1)

    #print(f"{changes_list}")
    print(f"{added_changes}")
    print(f"{average_changes}")

    #GOT IT!!!!!!!
    #print(f"{changes}")
    #The greatest increase in profits (date and amount) over the entire period
    # somehow finding biggest number in profits/losses column and identifying the date


    #The greatest decrease in losses (date and amount) over the entire period
    # # somehow finding smallest number in profits/losses column and identifying the date


    # want to both print report to the terminal and create text file with the results.



#printing

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {number_of_months}")
print(f"Total: {'${}'.format(net_amount)}")
#print(f"Average Change: {'${}'.format(average)}")






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