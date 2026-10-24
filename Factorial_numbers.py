n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#IN RANGE LIKE(1,5)

a=int(input())
b=int(input())
for i in range(a,b+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print(fact)
