n = int(input())
a = input().split()
last = a[-1]
other = a[:-1]
result = [last] + other 
print(*result) 
