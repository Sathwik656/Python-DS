n = int(input("Enter n: "))
lis=[]
for i in range(n):
    num = int(input("Enter values: "))
    lis.append(num)
    
max_v=lis[0]
min_v=lis[0]

for i in lis:
    if i> max_v:
        max_v = i
    if i< min_v:
        min_v = i
        
print(lis)
print("Max: ",max_v)
print("Min: ",min_v)