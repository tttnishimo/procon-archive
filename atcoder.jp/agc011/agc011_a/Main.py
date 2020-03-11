n,c,k = map(int, input().split())
a = []
bus = 1
for i in range(n):
  a.append(int(input()))
a.sort()

j = 0
count = 1
while j + count in range(n):
  if a[j + count] <= a[j] + k and count < c:
    count = count + 1
  else:
    bus = bus + 1
    j = j + count
    count = 1
print(bus)