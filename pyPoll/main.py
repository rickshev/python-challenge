import os
import csv

# variables - total number of votes and number of votes cast for respective candidates
total = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
tooley_votes = 0

# open file path
filepath = os.path.join("Resources/election_data.txt")

# read file as csvfile with header and rows
with open(filepath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    row = next(csvreader)

    total += 1    # start index 0 with value 1

    # for loop to read through rows
    for row in csvreader:

        # total votes
        total += 1

        # Khan votes
        if row[2] == "Khan":
            khan_votes += 1
        # Correy votes
        elif row[2] == "Correy":
            correy_votes += 1
        # Li votes
        elif row[2] == "Li":
            li_votes += 1
        # O'Toole votes
        else:
            tooley_votes += 1
        
        # percentage of votes for Khan, Correy, Li, and O'Tooley, respectively

        khan_percentage = khan_votes / total
        correy_percentage = correy_votes / total
        li_percentage = li_votes / total
        tooley_percentage = tooley_votes / total

        # determine most votes
        most = max(khan_votes, correy_votes, li_votes, tooley_votes)

        # determine winner name
        if most == khan_votes:
            winner = "Khan"
        elif most == correy_votes:
            winner = "Correy"
        elif most == li_votes:
            winner = "Li"
        else:
            winner = "O'Tooley"



# print results summary/analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total}")
print("-------------------------")
print(f"Khan: {khan_percentage:.3%} ({khan_votes})")
print(f"Correy: {correy_percentage:.3%} ({correy_votes})")
print(f"Li: {li_percentage:.3%} ({li_votes})")
print(f"O'Tooley: {tooley_percentage:.3%} ({tooley_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# write text file to display and store poll results summary
output_path = os.path.join("Results/summary.txt")    # file path

with open(output_path, 'w') as txtfile:    # write exported file (,'w')
    
    # REMEMBER '\n' to skip line
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total}\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Khan: {khan_percentage:.3%} ({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percentage:.3%} ({correy_votes})\n")
    txtfile.write(f"Li: {li_percentage:.3%} ({li_votes})\n")
    txtfile.write(f"O'Tooley: {tooley_percentage:.3%} ({tooley_votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
