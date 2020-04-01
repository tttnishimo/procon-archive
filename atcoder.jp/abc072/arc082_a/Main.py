n = int(input())
a = list(map(int, input().split()))
b = [0] * (pow(10,5) + 1)
for i in range(n):
  if a[i] == 0:
    b[0] += 1
    b[1] += 1
  elif a[i] == pow(10,5):
    b[pow(10,5) - 1] += 1
    b[pow(10,5)] += 1
  else:
    b[a[i]] += 1
    b[a[i] - 1] += 1
    b[a[i] + 1] += 1
print(max(b))