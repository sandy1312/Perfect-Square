import math
n=int(input("Enter last number:"))
for i in range(1,n):
    c=math.pow(i,2)
    if c>=n:
        break
    print(c)