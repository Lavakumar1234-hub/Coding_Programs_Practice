n=int(input()) #23,1321
temp=n
product=1
while temp>0:
    digit=temp%10
    product=digit*product
    temp//=10
result=product+n
np=n+1
while True:
    count=0
    for i in range(1,np+1):
        if np%i==0:
            count+=1
    if count==2:
        break
    np+=1
if result==np:
    print("Pointer Prime")
else:
    print("Not a Pointer Prime")