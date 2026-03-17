a = int(input())
i = 0
while i*i <= 50:
    if 2**i < a:
        print(2**i, end =" ")
    i+=1