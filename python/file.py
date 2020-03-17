import csv
from collections import defaultdict
import pandas as pd

filename = 'export_dataframe.csv'

dct = {}
dup = []
l = 0 #for checking a count of rows

df = pd.read_csv(filename)
df = df.transpose() #convering a dataframe from column to row strecture

''' Code For removing the duplicate entry : Strat'''
for index, row in df.iterrows():
	l += 1
	ch = index
	if index.find("www.") >= 0:
		ch = index.split("www.")[1]

	if ch in dct:
		dup.append(ch)
	else:
		dct[ch] = [row]
''' Code For removing the duplicate entry : End'''

''' Code For write a file in csv format with dictionary: Strat'''
'''with open('New_File2.csv', 'w') as f:
	for key in dct.keys():
        	f.write("%s,%s,%s,%s,%s,%s\n"%(key,dct[key][0][0],dct[key][0][1],dct[key][0][2],dct[key][0][3],dct[key][0][4]))
'''
#print(l)
#print(len(dct))
#print(dup)

''' Code For write a file in csv format with dictionary: End'''

''' Code For write dataframe to a csv file : Strat'''
#df.to_csv("New_File1.csv")
''' Code For write dataframe to a csv file : End'''
