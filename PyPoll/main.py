#list modules for script
import csv
import os


#declares variables for script
Totalvotes = 0
Candidatelist = {}
Percentagewon = []
Winner = ''
Mostvotes = 0

#csvpath to open file
csvpath = os.path.join('PyPoll/Resources/election_data.csv')


#open csv file to analyze
with open(csvpath) as csvfile:


    #read csv file
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #skip first row header

    csvheader = next(csvreader)

    #analyze each row after header 
    for row in csvreader:

        Candidate = row[2]

        #tally votes for each candidate
        Totalvotes += 1


        #list of Candidates in Election
        if Candidate in Candidatelist:
            Candidatelist[Candidate] += 1

        else: 
            Candidatelist[Candidate] = 1

print('Election Results')
print('---------------------------')
print('Total Votes:', Totalvotes)
print('----------------------------')

for Candidate, votes in Candidatelist.items():
    Percentagewon = round((votes / Totalvotes) * 100, 2)
    print(Candidate, Percentagewon, votes)   
    
    if Mostvotes < votes:
        Mostvotes = votes
        Winner = Candidate

print('-----------------------------')
print('Winner:', Winner)    
print('------------------------------')


#path for text file export
textpath = os.path.join('PyPoll/Analysis/PyPoll Text File.txt')

with open(textpath,'w') as csvfile:

    #csvwriter = csv.writer(csvfile, delimiter=',')

    csvfile.write(f"Election Results\n")
    csvfile.write(f"---------------------------\n")
    csvfile.write(f"Total Votes, {Totalvotes}\n")
    csvfile.write(f"----------------------------\n")

    for Candidate, votes in Candidatelist.items():
        Percentagewon = round((votes / Totalvotes) * 100, 2)
        csvfile.write(f"{Candidate} {Percentagewon} {votes}\n")   
    
        if Mostvotes < votes:
            Mostvotes = votes
            Winner = Candidate

    csvfile.write(f"-----------------------------\n")
    csvfile.write(f"Winner: {Winner}\n")    
    csvfile.write(f"------------------------------")