a=int(input())
b=int(input())
k=max(a,b)
h=k
while True:
    if k%a==0 and k%b==0:
        print("LCM =",k)
        break
    k=k+h

#USING EUCLIDEAN THEOREM
a=int(input())
b=int(input())
x=a #a value
y=b #b value
while y!=0:
    x,y=y,x%y
hcf=x
lcm=(a*b)//hcf
print(lcm)