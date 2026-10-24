#USING COUNT

n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("Prime Number")
else:
    print("Not a Prime Number")

#WITHOUT COUNT

n=int(input())
for i in range(2,n):
    if n%i==0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")

#IN RANGE LIKE(1,10):2,3,5,7

a=int(input())
b=int(input())
for i in range(a,b+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=" ")

#IN PATTERN(HORIZONTAL)

n=5
num=2
total=n*n+1//2
l=[]
while len(l)<total:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        l.append(num)
    num+=1
k=0
for i in range(1,n+1):
    for j in range(1,i+1):
        print(l[k],end=" ")
        k+=1
    print()

#IN PATTERN(VERTICAL)
n=5
num=2
total=n*n+1//2
l=[]
while len(l)<total:
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count==2:
        l.append(num)
    num+=1
for i in range(n):
    index=i
    for j in range(i+1):
        print(l[index],end=" ")
        index+=n-j-1
    print()






