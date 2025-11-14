def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
n = int(input("Enter n: "))
r = int(input("Enter r: "))
if n<0:
    print("Inlvaid input")
else:
    print("Ncr = ",fact(n)//(fact(r)*fact(n-r)))