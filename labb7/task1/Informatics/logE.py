v = int(input())
i = 0
while v > i:
    if 2**i >=v:
        print(i)
        break
    i+=1
