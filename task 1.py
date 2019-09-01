"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
row1=[]
row2=[]

r1=[]
r2=[]
r3=[]
r4=[]

for row1 in texts:
    r1=r1+(row1[0].split(","))
    r2=r2+(row1[1].split(","))
    
for row2 in calls:
    r3=r3+(row2[0].split(","))
    r4=r4+(row2[1].split(","))

unique_list = []
unique_list=set(r1+r2+r3+r4)


print('"There are ',len(unique_list),' different telephone numbers in the records."')


      

