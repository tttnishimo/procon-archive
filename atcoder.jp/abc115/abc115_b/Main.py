n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
print(sum(a)-max(a)//2)