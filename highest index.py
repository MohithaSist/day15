'''a=input()
l1=[]
for i in a:
    
    m=ord(i)
    l1.append(m)
    print(l1)
print(max(l1)-96,chr(max(l1)))'''

import json
a=input()
l1=[]
if a.isupper():
    a=a.lower()
for i in a:
    m=ord(i)
    l1.append(m)
print(l1)
c=len(l1)
o=l1[0]
for i in range(0,len(l1)-1):
    if l1[i]>o:
        o=l1[i]
n=str(o-96)+chr(o)
print(json.dumps(n))







'''a=[1,453,4,4,76,3,34,233]
l1=[]
m=a[0]
for j in range(0,len(a)-1):
        if m<a[j]:
            m=a[j]
print(m)'''



    
