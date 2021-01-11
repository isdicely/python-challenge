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
    #print(f"CSV Header: {election_data_header}")

    # This dictionary will hold the candidates names as the key and the values will be the total votes
    candidates_dict = {}

    # Iterate through all rows
    # Collecting candidate names into a dictionary and their total votes
    for row in election_data:
        if row[2] not in candidates_dict:
            candidates_dict[row[2]] = 1
        else:
            candidates_dict[row[2]] +=1
            
    # Calcuate total votes cast
    total_votes = sum(candidates_dict.values())
    
    # make list of candidates
    candidates = list(candidates_dict.keys())
    
    # Percentage of votes for each candidate
    # Dictionary comprehension
        # Calculates vote percents as it iterates through the keys (candidates) and uses the values (total votes)
    vote_percents = {candidate: votes/total_votes*100 for candidate, votes in candidates_dict.items() }
    
    # Find winner (most votes cast)
    # Used operator module to use the itemgetter function
    # sorting by the values of candidates_dict, returning the candidate name
    election_winner = max(candidates_dict.items(),key = operator.itemgetter(1))[0]

    # Print the analysis summary        
    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: {total_votes}')
    # Iterate through the dictionaries to get the folowing values from the key(candidate names)
    print("----------------------------")
    for key, value in vote_percents.items():
        print(f'{key}: {value:0.3f}% ({candidates_dict[key]})')
    print("----------------------------")
    print(f'Winner: {election_winner}')
    print("----------------------------")

    # Write the analysis summary to a txt file
    with open('Analysis/PyPoll_analysis.txt', mode = 'w') as PyPoll_analysis:
        print("Election Results",file=PyPoll_analysis)
        print("----------------------------",file=PyPoll_analysis)
        print(f'Total Votes: {total_votes}',file=PyPoll_analysis)
        # Iterate through the dictionaries to get the folowing values from the key(candidate names)
        print("----------------------------",file=PyPoll_analysis)
        for key, value in vote_percents.items():
            print(f'{key}: {value:0.3f}% ({candidates_dict[key]})',file=PyPoll_analysis)
        print("----------------------------",file=PyPoll_analysis)
        print(f'Winner: {election_winner}',file=PyPoll_analysis)
        print("----------------------------",file=PyPoll_analysis)
