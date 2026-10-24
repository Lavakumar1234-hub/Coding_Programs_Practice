n=int(input())
def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
after=n+1
before=n-1
while True:
    if is_prime(after):
        break
    after+=1
while True:
    if is_prime(before):
        break
    before-=1
if (after-n)<(n-before):
    print("Nearest Prime Number :",after)
elif (after-n)>(n-before):
    print("Nearest Prime Number :",before)
else:
    print("Nearest Prime Numbers :",before,after)
