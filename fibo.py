"""def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(10))
"""


f1=0
f2=1
fibo=0
list=[]
n=int(input("enter the n number"))
for a in range(0,n):
    num=int(input("enter the number"))
    list.append(num)

for b in list:
    for i in range(2, b):
        fibo = f1 + f2
        f1 = f2
        f2 = fibo
        print(fibo)
        
    

list.clear()

    
