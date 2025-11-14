def sum_of_digits(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s

n = int(input("Enter n: "))
max_sum=0
for i in range(1,n+1):
    num=int(input(f"Enter number {i}: "))
    s=sum_of_digits(num)
    if s > max_sum:
        max_sum=s
print("Maximum sum of digits: ",max_sum)