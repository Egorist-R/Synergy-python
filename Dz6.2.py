import math 
X = int(input())
count = 0
for i in range(1, int(math.isqrt(X)) +1):
    if X % i == 0:
        if i * i == X:
            count += 1
        else:
            count += 2
print(count) 