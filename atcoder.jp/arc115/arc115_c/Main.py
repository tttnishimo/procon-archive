n=int(input())
a=[1]
for i in range(17):
  t=a[-1]+1
  for j in range(2**(i+1)):
    a.append(t)
print(*a[:n])