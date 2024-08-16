a='a1b3c4'
b=[]
d=[]
c=""
for i in a:
    if i.isnumeric()==True:
        b.append(int(i))

for j in a:
    if j.isalpha()==True:
        d.append(j)
for i in range(len(d)):
    c += d[i] * b[i] 
        
                
print(c)    
