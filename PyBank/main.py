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
    #The net total amount of "Profit/Losses" over the entire period
    # Calculate the changes in "Profit/Losses" over the entire period, 
    # then find the average of those changes
    
    # num_months will hold the number of months in the data set after running the for loop.
    # mon_year holds the date
    # sum_profits_losses will hold the sum of the profits and losses
    # delta_profits_losses will hold the difference between the profits and losses
        # this will help calculate the average of the difference
    num_months = 0
    mon_year = ""
    sum_profits_losses = 0
    previous_profit_loss_value = None
    current_profit_loss_value = 0
    delta_profits_losses = 0
    sum_delta_profits_losses = 0
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
    # Calculate the average of the changes in the profit/losses
    ave_delta_profits_losses = sum_delta_profits_losses/(num_months-1)

        
    print(num_months)
    print(sum_profits_losses)
    print(ave_delta_profits_losses)
