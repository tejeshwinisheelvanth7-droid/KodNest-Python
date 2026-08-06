n = int()
l =[]
for i in range(n):
    m = int(input())
    l.append(m)
pos_count = 0
neg_count = 0
zeros = 0
total = 0
for i in l:
    if i > 0:
        pos_count += 1
        total += i
    elif i < 0:
        neg_count += 1
        total += i
    else:
        zeros += 1
print("Positive Count:",pos_count)
print("Negative Count:",neg_count)
print("Zero Count:",zeros)
print("Total:",total)