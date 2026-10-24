num=input() #197
prime=True
for i in range(len(num)):
    l=num[i:]+num[:i]
    n=int(l)
    if n<2:
        prime=False
        break
    for j in range(2,int(n**0.5)+1):
        if n%j==0:
            prime=False
            break
    if prime:
        break
if prime:
    print("Circular Prime")
else:
    print("Not a Circular Prime")


