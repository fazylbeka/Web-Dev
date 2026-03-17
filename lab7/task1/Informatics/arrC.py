n = int(input())
# Read all numbers from one line and convert to integers
arr = list(map(int, input().split()))

count = 0
for x in arr:
    if x > 0:  # Positive means > 0
        count += 1

print(count)
