n = int(input("Enter a number: "))
if n<0:
    print("Invalid input")
else:
    temp = n
    rev = 0
    while temp > 0:
        rev=rev*10+(temp%10)
        temp//=10
    if rev==n:
        print("Palindrome number")
    else:
        print("Not a palindrome")


