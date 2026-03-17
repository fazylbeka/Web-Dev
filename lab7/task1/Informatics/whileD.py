n = int(input())

while n >= 1:
    if n%2 !=0:
        break
    n = n // 2
    
if n == 1:
    print("YES")
else:
    print("NO")