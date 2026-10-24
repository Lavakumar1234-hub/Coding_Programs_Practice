n=int(input())
x=n-1
while True:
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    if count==2:
        print("Before Prime Number :",x)
        break
    x-=1

#USING FUNCTION

n=int(input())
def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
x=n-1
while True:
    if is_prime(x):
        print("Before Prime Number :",x)
        break
    x-=1