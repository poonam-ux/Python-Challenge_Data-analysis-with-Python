# Import modules/dependencies
import os
import csv

# Create variables
total_months = 0
total_amount = 0
greatest_increase = 0
greatest_decrease = 9999999999999
monthly_change = []
month_of_change = []
greatest_increase_month = 0
greatest_decrease_month = 0

# Set path for file
budget_csv = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Open and Read CSV file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)
    first_row = next(csvreader)
    
    # Calculate total number of months, total amount of "Profit/Losses"
    total_months = total_months + 1
    total_amount = total_amount + int(first_row[1])
    prev_amount = int(first_row[1])
    
    # Read through each row after the header
    for row in csvreader:
        
        # Calculate total number of months
        total_months = total_months + 1

        # Calculate total amount of "Profit/Losses" over the entire period
        total_amount = total_amount + int(row[1])

        # Calculate Change
        net_change = int(row[1]) - prev_amount
        prev_amount = int(row[1])
        monthly_change.append(net_change)
        month_of_change.append(row[0])
        
        # Calculate the greatest increase
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = row[0]
            
        # Calculate the greatest decrease
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = row[0]  
        
    # Calculate the average
    monthly_average_change = sum(monthly_change)/ len(monthly_change)

# Print analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${monthly_average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${greatest_increase})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${greatest_decrease})")

# Specify file to Write To
budget_analysis = os.path.join('..', 'PyBank', 'Analysis', 'budget_data_analysed.txt')

# Open file using "Write" mode. Specify the variable to hold the contents
with open(budget_analysis, 'w',) as analysedfile:

# Write new data
    analysedfile.write(f"Financial Analysis\n")
    analysedfile.write(f"---------------------------\n")
    analysedfile.write(f"Total Months: {total_months}\n")
    analysedfile.write(f"Total: ${total_amount}\n")
    analysedfile.write(f"Average Change: ${monthly_average_change:.2f}\n")
    analysedfile.write(f"Greatest Increase in Profits: {greatest_increase_month}, (${greatest_increase})\n")
    analysedfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${greatest_decrease})\n")