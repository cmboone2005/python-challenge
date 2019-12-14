import csv
import os

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

def checkIfDuplicates_1(voters):
    if len(voters) == len(set(voters)):
        return False
    else:
        return True

result = checkIfDuplicates_1(voters)
 
if result:
    print('Some voters voted more than once')
else:
    print('Every voter only voted once')
       