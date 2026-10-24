a=int(input())
b=int(input())
k=min(a,b)
for i in range(k,0,-1):
    if a%i==0 and b%i==0:
        print("HCF =",i)
        break

#USING EUCLIDEAN THEOREM

a=int(input())
b=int(input())
x=a #a value
y=b #b value
while y!=0:
    x,y=y,x%y
hcf=x
print("HCF =",hcf)

