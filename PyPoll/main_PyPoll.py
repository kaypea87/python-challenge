#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 00:16:37 2024

@author: Komie
"""

import pandas as pd
from pathlib import Path

#path to csv file and read
election_data = Path("Resources/election_data.csv")
election_df = pd.read_csv(election_data)
election_df.head()

#The total number of votes cast
totalvotes = len(election_df)

#A complete list of candidates who received votes, unique values
candidate_list = election_df['Candidate'].unique()

#The percentage of votes each candidate won
#The total number of votes each candidate won
#create candidate votes dictionary
candidate_votes = {}

for candidate in candidate_list:
    candidate_votes[candidate]=0

for i in range(totalvotes):
    name = election_df['Candidate'][i]
    candidate_votes[name] = candidate_votes[name] +1

#create votepercent dictionary to track the percentages
votepercent={}
for candidate in candidate_votes: 
    votepercent[candidate] = candidate_votes[candidate] / totalvotes

#The winner of the election based on popular vote using max value in dictionary
#source: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
maxvotes = max(candidate_votes, key=candidate_votes.get)

print("Elections Results")
print("-----------------------")
print(f"Total Votes: {totalvotes}")
print("-----------------------")
for candidate in candidate_list:
    print(f"{candidate} : {votepercent[candidate]:.3%} ({candidate_votes[candidate]})")
print("-----------------------")
print(f"Winner: {maxvotes}")
print("-----------------------")

#write fiile to text
file = open('analysis/output.txt','w',encoding ='UTF-8')
file.write("Election Results")
file.write("-----------------------")
file.write(f"Total Votes: {totalvotes}")
file.write("-----------------------")
for candidate in candidate_list:
    file.write(f"{candidate} : {votepercent[candidate]:.3%} ({candidate_votes[candidate]})")
file.write("-----------------------")
file.write(f"Winner: {maxvotes}")
file.write("-----------------------")
file.close()










