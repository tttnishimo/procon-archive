a,b = map(int, input().split())
c = list(map(int, input().split()))
for i in range(b):
  a = a - c[i]
if a > 0:
  print("No")
else:
  print("Yes")