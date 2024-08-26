'''
x={}

for i in range(0,4):
    n=input("enter your name")
    a=int(input("enter your age"))
    if 'Name' in x:
        x['Name'].append(n)
    else:
        x['Name']=[]
    if 'Age' in x:
        x['Age'].append(a)
    else:
        x['Age']=[]
    

print(x)
'''

student={}

no_std=int(input("enter no of students"))
no_sub=int(input("enter no of subjects"))

for i in range(no_std):
    name=input("enter name of students")
    


    result={}

    for i in range(no_sub):
        sub=input("enter name of subjecta")
        mark=int(input("enter marks"))
        result[sub]=mark

    

    student[name]=result





print(student)











