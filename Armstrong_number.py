n=int(input()) #1to9,153
temp=n
dc=0
while temp>0:
    dc+=1
    temp//=10
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**dc
    temp//=10
if sum==n:
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")

