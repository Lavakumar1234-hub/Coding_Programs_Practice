n=int(input())
a=0
b=1
count=0
while count<n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count+=1

#IN PATTERN
n=int(input())
a=0
b=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
    print()