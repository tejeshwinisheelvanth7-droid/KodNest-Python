limit = int(input())
target = int(input())
count = 0
total = 0
found = "No"
for i in range(1,   limit+1):
    if i % 3 == 0:
        count += limit
        total += i
        if i == target:
            found = "Yes"
print("Count:",count)
print("Sum:",total)
print("Found Target:",found)
  