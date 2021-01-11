# Import OS module:
# The OS module provides a way to use operating system dependent functionality.
# This allows us to create file paths to access files
import os
# Import module for reading CSV files. 
# This allows us to read and write tabular data in CSV format.
import csv
# Set path to retrieve csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Test that path is correct and read file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    budget_data = csv.reader(csvfile)
    # Read the header row first
    budget_data_header = next(budget_data)
    print(f"CSV Header: {budget_data_header}")
    # Calculate the number of months in the data set
    # The net total amount of "Profit/Losses" over the entire period
    # Calculate the changes in "Profit/Losses" over the entire period, 
        #then find the average of those changes
    # Find the greatest increase in profits (date and amount) over the entire period
    # Find the greatest decrease in losses (date and amount) over the entire period
    # num_months will hold the number of months in the data set after running the for loop.
    # mon_year holds the date
    # sum_profits_losses will hold the sum of the profits and losses
    # previous_profit_loss_value, current_profit_loss_value, delta_profits_loss_value,
        # sum_delta_profits_losses will help calculate the average of the difference
    # greatest_profit_increase and greatest_loss_decrease varibles to help identify these these values
        # date_grtst_profit_inc and date_grtst_loss_dec will hold the date when these values occured
        
    num_months = 0
    mon_year = ""
    sum_profits_losses = 0
    previous_profit_loss_value = None
    current_profit_loss_value = 0
    delta_profits_losses = 0
    sum_delta_profits_losses = 0
    greatest_profit_increase = 0
    greatest_loss_decrease = 0
    date_grtst_profit_inc = ""
    date_grtst_loss_dec = ""

    # Iterate through all rows
    for row in budget_data:
        # Count the number of months in the data set
        if row[0] != mon_year:
            num_months += 1
            mon_year = row[0]
        # Change data type of the Profits/Losses from string to integer.
        profit_loss = int(row[1])
        #Sum up the profits/losses to get the net total amount.
        sum_profits_losses += profit_loss
        # Calculate the difference of the profits/losses
        current_profit_loss_value = profit_loss
        if previous_profit_loss_value is not None:
            delta_profits_losses = current_profit_loss_value - previous_profit_loss_value
            # Add up the sum of the difference of profits/losses
            sum_delta_profits_losses += delta_profits_losses
        # Reset previos profit/losses variable
        previous_profit_loss_value = current_profit_loss_value
        # Find the greatest profit and loss 
        # Hold the date of these values
        if delta_profits_losses > greatest_profit_increase:
            greatest_profit_increase = delta_profits_losses
            date_grtst_profit_inc = mon_year
        if delta_profits_losses < greatest_loss_decrease:
            greatest_loss_decrease = delta_profits_losses
            date_grtst_loss_dec = mon_year
    # Calculate the average of the changes in the profit/losses
    ave_delta_profits_losses = sum_delta_profits_losses/(num_months-1)

    # Print Analysis report
    print("Financial Analysis")
    print("-------------------------------------------------")
    print(f'Total Months: {num_months}')
    print(f'Total: ${sum_profits_losses}')
    print(f'Average Change: ${ave_delta_profits_losses:0.2f}')
    print(f'Greatest Increase in Profits: {date_grtst_profit_inc} (${greatest_profit_increase})')
    print(f'Greatest Decrease in Profits: {date_grtst_loss_dec} (${greatest_loss_decrease})')

    # Write analysis to text file
    with open('Analysis/PyBank_analysis.txt', mode = 'w') as PyBank_analysis:
        print("Financial Analysis",file=PyBank_analysis)
        print("-------------------------------------------------",file=PyBank_analysis)
        print(f'Total Months: {num_months}',file=PyBank_analysis)
        print(f'Total: ${sum_profits_losses}',file=PyBank_analysis)
        print(f'Average Change: ${ave_delta_profits_losses:0.2f}',file=PyBank_analysis)
        print(f'Greatest Increase in Profits: {date_grtst_profit_inc} (${greatest_profit_increase})',file=PyBank_analysis)
        print(f'Greatest Decrease in Profits: {date_grtst_loss_dec} (${greatest_loss_decrease})',file=PyBank_analysis)