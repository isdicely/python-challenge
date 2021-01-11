# Import operator module:
# Provides functions that allows to get number or touple from list
import operator
# Import OS module:
# The OS module provides a way to use operating system dependent functionality.
# This allows us to create file paths to access files
import os
# Import module for reading CSV files. 
# This allows us to read and write tabular data in CSV format.
import csv
# Set path to retrieve csv file
csvpath = os.path.join('Resources', 'Resources_election_data.csv')

# Test that path is correct and read file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    election_data = csv.reader(csvfile)
    # Read the header row first
    election_data_header = next(election_data)
    print(f"CSV Header: {election_data_header}")

    candidates_dict = {}

    # Iterate through all rows
    # Collecting candidate names into a dictionary and their total votes
    for row in election_data:
        if row[2] not in candidates_dict:
            candidates_dict[row[2]] = 1
        else:
            candidates_dict[row[2]] +=1
    print(candidates_dict)        
    # Calcuate total votes cast
    total_votes = sum(candidates_dict.values())
    print(total_votes)
    # make list of candidates
    candidates = list(candidates_dict.keys())
    print(candidates)
    # Percentage of votes for each candidate
    # Dictionary comprehension
        # Calculates vote percents as it iterates through the keys (candidates) and uses the values (total votes)
    vote_percents = {candidate: votes/total_votes*100 for candidate, votes in candidates_dict.items() }
    print(vote_percents)
    # Find winner (most votes cast)
    # Used operator module to use the itemgetter function
    # sorting by the values of candidates_dict, returning the candidate name
    election_winner = max(candidates_dict.items(),key = operator.itemgetter(1))[0]
    print(election_winner)
        


