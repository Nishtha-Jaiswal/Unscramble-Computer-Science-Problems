"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
#print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

maxm=0
long=[]
row2=[]
r2=[]
r3=[]
r4=[]
r5=[]
for row2 in calls:
    r2=r2+(row2[0].split(","))#calling no
    r3=r3+(row2[1].split(","))#receiving no
    r4=r4+(row2[2].split(","))#call date n time
    r5=r5+(row2[3].split(','))#call duration
    
    
list_list=[r2,r3,r5]


unique_list=[]
unique_list =unique_list+[(r2[0])]


for r2_i in range(len(r2)):
    
    chk=False
    
    for u_i in range(len(unique_list)):
        if r2[r2_i]==unique_list[u_i] :
            chk=True
    if chk==False:
            unique_list=unique_list+[r2[r2_i]]

            
for r3_i in range(len(r3)):
    
    chk=False
    
    for u_i in range(len(unique_list)):
        if r3[r3_i]==unique_list[u_i] :
            chk=True
    if chk==False:
            unique_list=unique_list+[r3[r3_i]]
            

for k in range(len(unique_list)):
    s=0
    for i in range(len(list_list[0])):
        
        
        if (unique_list[k]==list_list[0][i] or unique_list[k]==list_list[1][i]):
            s+= int(list_list[2][i])
            
    long+=[s]

maxm=max(long)
indices = [z for z, x in enumerate(long) if x == maxm]

#output
print('"',unique_list[indices[0]]," spent the longest time, ", maxm ,' seconds, on the phone during September 2016."')

