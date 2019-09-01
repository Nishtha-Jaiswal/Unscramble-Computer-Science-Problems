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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""




row2=[]
r2=[]#callers list
r3=[]#receiver list
r5=[]
r6=[]
r9=[]#list of area codes
r8=[]#list of prefix nos
unique_list_ac=[]#stores unique area codes
unique_list_pf=[]#stores unique prefix nos

for row2 in calls:
    r2=r2+(row2[0].split(","))#calling no
    r3=r3+(row2[1].split(","))#receiving no


list_list=[r2,r3]

for i in range(len(list_list[0])):
    if "080" in list_list[0][i]:
        if "(" in list_list[1][i]:   
            r5=r5+[list_list[1][i].split("(")[1]]
        
        if (" " in list_list[1][i]):   
            r6=r6+[list_list[1][i]]
            

for i in range(len(r6)):
    r8=r8+ [r6[i][:4]]    

for i in range(len(r5)):
    r9=r9+[r5[i].split(")")[0]]
    

for r9_i in range(len(r9)):
    
    chk=False
    
    for u_i in range(len(unique_list_ac)):
        if r9[r9_i]==unique_list_ac[u_i] :
            chk=True
    if chk==False:
            unique_list_ac=unique_list_ac+[r9[r9_i]]
            unique_list_ac=sorted(unique_list_ac)

    

for r8_i in range(len(r8)):
    
    chk=False
    
    for u_i in range(len(unique_list_pf)):
        if r8[r8_i]==unique_list_pf[u_i] :
            chk=True
    if chk==False:
            unique_list_pf=unique_list_pf+[r8[r8_i]]
            unique_list_pf=sorted(unique_list_pf)

print("The numbers called by people in Bangalore have codes:")
for i in range(len(unique_list_ac)):
    print(unique_list_ac[i])
for i in range(len(unique_list_pf)):
    print(unique_list_pf[i])   


count=0#counter to strore no of calls made to nos in Bangalore
for i in range(len(r5)):
    if "080" in r5[i]:
        count+=1

tot_call=len(r5)+len(r6)#total no of calls from Bangalore


percent=round((count/tot_call)*100,2)#percentage

print('"',percent,' percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore".')
