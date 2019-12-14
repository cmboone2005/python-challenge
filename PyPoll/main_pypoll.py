import os
import csv
import sys

stdoutOrigin=sys.stdout
sys.stdout=open("pypolltext.txt","w")

winner=""
most_votes = 0

with open("election_data.csv") as csvfile:
    readCSV=csv.reader(csvfile,delimiter=',')
    next(readCSV)
    voters=[]
    counties=[]
    candidates=[]
    candidate_votes={}

    for row in readCSV:
        voter_id=row[0]
        county=row[1]
        candidate=row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate]=candidate_votes[candidate]+1

        voters.append(voter_id)
        counties.append(county)
        #candidates.append(candidate)

total_votes=len(voters)

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes Cast: {total_votes}")
print(f"-------------------------")
for candidate in candidate_votes:
    votes=candidate_votes.get(candidate)
    vote_percent=round(float(votes)/float(total_votes)*100)

    if (votes > most_votes):
        most_votes = votes
        winner=candidate

    voter_results=f"{candidate}: {vote_percent: 3f}% ({votes})\n"
    print(voter_results, end="")

print(f"-------------------------")
print(f"Winner:  {winner}")
print(f"-------------------------")

sys.stdout.close()
sys.stdout=stdoutOrigin

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes Cast: {total_votes}")
print(f"-------------------------")
for candidate in candidate_votes:
    votes=candidate_votes.get(candidate)
    vote_percent=round(float(votes)/float(total_votes)*100)

    if (votes > most_votes):
        most_votes = votes
        winner=candidate

    voter_results=f"{candidate}: {vote_percent: 3f}% ({votes})\n"
    print(voter_results, end="")

print(f"-------------------------")
print(f"Winner:  {winner}")
print(f"-------------------------")

