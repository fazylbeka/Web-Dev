n = int(input())
m = int(input())
if(n%2 == 0):
    for i in range(n, m+1, 2):
        print(i, end = " ")
else:
    for i in range(n+1, m+1, 2):
        print(i, end= " ")