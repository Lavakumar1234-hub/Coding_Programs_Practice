n=int(input()) #14,19,197
temp=n
l=[]
while temp>0:
    digit=temp%10
    l.append(digit)
    temp//=10
l.reverse()
while True:
    s=sum(l)
    if s==n:
        print("Keith Number")
        break
    if s>n:
        print("Not a Keith Number")
        break
    l.append(s)
    l.pop(0)

