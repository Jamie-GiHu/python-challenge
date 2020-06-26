import csv

# Store the file path for budget_data.csv
file = 'c:/Users/foong/Google Drive/PREWORK_JT/python-challenge/python-challenge JT submission/python-challenge/PyPoll/Resources/election_data.csv'

# Open the file in "read" mode and store the contents 
with open(file, 'r', newline='', ) as input_file:

    csvreader = csv.reader(input_file, delimiter = ',')

    # Read header in first row and skip reader
    header = next(csvreader)
    
    # Create dictionary as 'd'
    d = {}

    for row in csvreader:

        voter_id = row[0]
        candidate = row[2]
        d[voter_id] = candidate

    # Total number of votes cast can be found by calculating number of rows in dictionary
    total_votes = len(d)

    # Create dictionary as 'v' to hold candidates as keys where the voter id is grouped by candidates
    v = {}
    
    for voter_id, candidate in sorted(d.items()):
        v.setdefault(candidate,[]).append(voter_id)

    # Create lists that holds candidate names, percentage of votes won by candidate and total number of votes by candidates
    candidate_list = list()
    candidate_list_pc = list()
    candidate_list_votes = list()
    
    # Find or calculate values to be stored in respective lists
    for key, value in v.items():
        candidate_name = key
        candidate_list.append(candidate_name)
        candidate_pc = ("%.3f"% (len(value)/total_votes*100))
        candidate_list_pc.append(candidate_pc)
        candidate_votes = len(value)
        candidate_list_votes.append(candidate_votes)

    # Winner of the election based on popular vote can be found by finding candidate with highest vote
    winner_index = candidate_list_votes.index(max(candidate_list_votes)) # To find position of highest votes in list
    winner = candidate_list[winner_index] # To find name of election winner by matching position in candidate name list

 # Print out the election results analysis
    print(f"Election Results")
    print(f"-" * 30)  
    print(f"Total Votes: {total_votes}")
    print(f"-" * 30)
    x = 0
    for candidate in range(len(candidate_list)):
        print(f"{candidate_list[x]}: {candidate_list_pc[x]}% ({candidate_list_votes[x]})")
        x += 1
    print(f"-" * 30)
    print(f"Winner: {winner}")
    print(f"-" * 30)

# Set variable for output file
output_file = 'c:/Users/foong/Google Drive/PREWORK_JT/python-challenge/python-challenge JT submission/python-challenge/PyPoll/analysis/election_results.txt'

#  Open the output file
with open(output_file, "w") as writer:

    # Write in election results analysis
    writer.write(f"Election Results")
    writer.write("\n")
    writer.write(f"-" * 30)
    writer.write("\n")  
    writer.write(f"Total Votes: {total_votes}")
    writer.write("\n")
    writer.write(f"-" * 30)
    writer.write("\n")
    x = 0 # Reset variable to 0
    for candidate in range(len(candidate_list)):
        writer.write(f"{candidate_list[x]}: {candidate_list_pc[x]}% ({candidate_list_votes[x]})\n")
        x += 1
    writer.write(f"-" * 30)
    writer.write("\n")
    writer.write(f"Winner: {winner}")
    writer.write("\n")
    writer.write(f"-" * 30)