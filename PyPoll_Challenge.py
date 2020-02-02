
#import dependencies

import csv
import os

# Accumulator variable

total_votes = 0
candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Largest county by vote count Tracker
county_largest_vote = ""
county_largest_vote_count = 0
county_largest_vote_percent = 0

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_results.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    
# Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
       # Get the candidate name and the county from each row.
        county_name = row[1]
        candidate_name = row[2]

        #Are we tracking the county yet
        if county_name not in county_options:
            #add to list of counties and initialize counter
            county_options.append(county_name)
            county_votes[county_name] = 0

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # count a vote
        candidate_votes[candidate_name] += 1 
        county_votes[county_name] += 1 

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    
    #county votes header
    county_results = (f"\nCounty Votes:\n")
    print(county_results, end="")
    txt_file.write(county_results)
    
    #loop through the counties
    for county in county_options:
        # build county results
        votes = county_votes[county]
        county_percent = float(votes) / float(total_votes) * 100
        #the calculation by county
        county_results = (f"{county}: {county_percent:.1f}% ({votes:,})\n")
        #print county results to terminal
        print(county_results, end="")
        #  Save the county results to our text file.
        txt_file.write(county_results)
    #largest county banner
        if (votes > county_largest_vote_count) and (county_percent > county_largest_vote_percent):
            county_largest_vote_count = votes
            county_largest_vote_percent = county_percent
            county_largest_vote = county
    largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {county_largest_vote}\n"
        f"-------------------------\n")
    print(largest_county_summary, end="")
    txt_file.write(largest_county_summary)
   
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
#  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate  
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)

