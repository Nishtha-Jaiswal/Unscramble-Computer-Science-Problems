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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

row1=[]
row2=[]

r1=[]
r2=[]
r3=[]
r4=[]
r5=[]
r6=[]

for row1 in texts:
    r1=r1+(row1[0].split(","))#nos sending text
    r2=r2+(row1[1].split(","))#nos receiving texts

for row2 in calls:
    r3=r3+(row2[0].split(","))#nos making call
    r4=r4+(row2[1].split(","))#nos receiving calls

unique_list=[]

for r1_i in range(len(r1)):
    
    chk=False
    
    for u_i in range(len(unique_list)):
        if r1[r1_i]==unique_list[u_i] :
            chk=True
    if chk==False:
            unique_list=unique_list+[r1[r1_i]]

for r2_i in range(len(r2)):
    
    chk=False
    
    for u_i in range(len(unique_list)):
        if r2[r2_i]==unique_list[u_i] :
            chk=True
    if chk==False:
            unique_list=unique_list+[r2[r2_i]]

for r4_i in range(len(r4)):
    
    chk=False
    
    for u_i in range(len(unique_list)):
        if r4[r4_i]==unique_list[u_i] :
            chk=True
    if chk==False:
            unique_list=unique_list+[r4[r4_i]]


unique_caller=[]

for r3_i in range(len(r3)):
    
    chk=False
    
    for u_i in range(len(unique_caller)):
        if r3[r3_i]==unique_caller[u_i] :
            chk=True
    if chk==False:
            unique_caller=unique_caller+[r3[r3_i]]

for i in range(len(unique_caller)):
    check=True
    for j in range(len(unique_list)):
        if(unique_caller[i]==unique_list[j]):
            check= False
    if check==True:
            r5=r5+[unique_caller[i]]
            
r5=sorted(r5)            
print("These numbers could be telemarketers: ")
for i in range(len(r5)):
    print(r5[i])


