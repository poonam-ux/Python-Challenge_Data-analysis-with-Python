# Import modules/dependencies
import os
import csv

# Create variables
total_votes = 0
candidate_name = []
unique_list = []
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Set path for file
csvpath = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Open and Read CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)

    # Read through each row of data after the header
    for row in csvreader:

        # Calculate total number of votes cast
        total_votes += 1
        candidate_name.append(row[2])

        # Calculate each candidate's total votes
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        else:
            otooley_votes += 1

    # Get list of candidate names
    for name in candidate_name: 
        # check if it exists in unique_list or not 
        if name not in unique_list:
            unique_list.append(name)

    # Calculate percentages of votes each candidate won
    khan_percent = khan_votes/total_votes
    correy_percent = correy_votes/total_votes
    li_percent = li_votes/total_votes
    otooley_percent = otooley_votes/total_votes

    # Find the winner
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"

# Print Analysis
print(f"Election Results")
print(f"--------------------------------")
print(f"Total Votes: {total_votes}")
print(f"Candidate Names: {unique_list}")
print(f"--------------------------------")
print(f"Khan: {khan_percent:.2%} (votes: {khan_votes})")
print(f"Correy: {correy_percent:.2%} (votes: {correy_votes})")
print(f"Li: {li_percent:.2%} (votes: {li_votes})")
print(f"O'Tooley: {otooley_percent:.2%} (votes: {otooley_votes})")
print(f"--------------------------------")
print(f"Winner is {winner_name} with {winner} votes!")
print(f"--------------------------------")
