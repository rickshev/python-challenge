# import os, csv to read file
import os
import csv

# variables
months = 0    # total months
money = 0    # net total
increase_month = 0    # month with largest increase
decrease_month = 0    # month with largest decrease
increase_most = 0    # greatest increase amount
decrease_most = 0    # greatest decrease amount
month_list = []    # list to store months with greatest increase/decrease
money_list = []    # list to store months' money amount
average = 0    # average amount of revenue per month

# open file path
filepath = os.path.join("Resources/budget_data.txt")

# read file as csvfile with header and rows
with open(filepath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    row = next(csvreader)

    # setting variable locations on csvfile
    months += 1    # increase month by 1
    money += int(row[1])    # add revenue values and go to next
    last_month = int(row[1])    # for measuring greatest revenue changes 
    increase_most = int(row[1])    # total amount for month with greatest increase
    increase_month = row[0]    # month with greatest increase
    decrease_most = 0    # total amount for month with greatest decrease
    decrease_month = 0    # month with greatest decrease

    
    # for loop to read throw rows
    for row in csvreader:

        months += 1    # count total number of months

        money += int(row[1])    # count total amount of money by adding each row together

        # calculating greatest monthly revenue change
        month_change = int(row[1]) - last_month
        money_list.append(month_change)
        last_month = int(row[1])    # reset last_month variable to compare for next for loop iteration
        month_list.append(row[0])

        # average Profit/Loss
        average = sum(money_list) / len(money_list)

        # greatest increase month
        if int(row[1]) > increase_most:
            increase_most = int(row[1])
            increase_month = row[0]
        
        # greatest decrease month
        if int(row[1]) < decrease_most:
            decrease_most = int(row[1])
            decrease_month = row[0]
        

    
# printing the summary analysis
print("Financial Analysis")
print("---------------------------------------")
print(f"Total months: {months}")
print(f"Total: {money}")
print(f"Average Change: {average:.2f}")
print(f"Greatest Increase in Profits: {increase_month} ({max(money_list)})")
print(f"Greatest Decrease in Profits: {decrease_month} ({min(money_list)})")

# write text file to display and store the summary results
output_path = os.path.join("Results/summary.txt")    # output file path

with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------------------\n")
    txtfile.write(f"Total months: {months}\n")
    txtfile.write(f"Total: {money}\n")
    txtfile.write(f"Average Change: {average:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {increase_month} ({max(money_list)})\n")
    txtfile.write(f"Greatest Decrease in Profits: {decrease_month} ({min(money_list)})\n")
