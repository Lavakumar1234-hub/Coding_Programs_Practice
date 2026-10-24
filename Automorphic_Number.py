n=int(input()) #25*25=625 --> 25==25
sq=n*n
dc=len(str(n))
if (sq%10**dc)==n:
    print("Automorphic Number")
else:
    print("Not a Automorphic Number")
