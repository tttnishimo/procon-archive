n = int(input())
a = list(map(int, input().split()))
a.sort()
bars = [0,0]
for i in range(n-1):
  if a[i + 1] == a[i]:
    bars.pop(0)
    bars.append(a[i])
    a[i+1] = 0
print(bars[0]*bars[1])