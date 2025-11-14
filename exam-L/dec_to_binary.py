def to_binary(n):
    if n==0:
        return "0"
    binary=""
    while n>0:
        binary=str(n%2)+binary
        n//=2
    return binary

n=int(input("Enter a decimal number: "))
print("Binary equivalent =",to_binary(n))
