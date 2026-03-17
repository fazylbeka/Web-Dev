n = input()
sum = 0
power = 0
for digit in reversed(n):
    if digit == '1':
        sum+=2**power
    power+=1
print(sum)