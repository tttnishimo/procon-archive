a = [1,1,1]
n = int(input())
for i in range(n):
  a.append(a[-1]+a[-2])
if n == 0:
  print(1)
else:
  print(sum(a[:n]))