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
    num_months = 0
    mon_year = ""
    for row in budget_data:
        if row[0] != mon_year:
            num_months += 1
            mon_year = row[0]
    print(num_months)
