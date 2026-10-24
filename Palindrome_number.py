n=int(input())
temp=n
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp//=10
if rev==n:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

#IN RANGE(100,150) #101,111,121,131,141

a=100
b=150
for i in range(a,b+1):
    temp=i
    rev=0
    while temp>0:
        digit=temp%10
        rev=rev*10+digit
        temp//=10
    if rev==i:
        print(i)

