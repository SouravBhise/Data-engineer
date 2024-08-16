count=0
v=['a','e','i','o','u']
a=input('enter a sentence')
b=a.lower()

for i in v:
    if i in b:
        count+=1
print(count)
