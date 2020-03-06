a,b = map(int, input().split())
max = 0
arr = list(map(int, input().split()))
cumsum = [0] * (a + 1)
for i in range(a):
  cumsum[i+1] = cumsum[i] + arr[i]
for i in range(a - b + 1):
  sum = 0
  sum = cumsum[i + b] - cumsum[i]
  if sum > max:
    max = sum
print((max + b) / 2)