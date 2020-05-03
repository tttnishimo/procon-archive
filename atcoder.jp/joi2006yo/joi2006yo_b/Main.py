n = int(input())
dict = {}
for i in range(n):
  a,b = map(str, input().split())
  dict[a] = b
m = int(input())
res = ''
for i in range(m):
  a = input()
  if a in dict:
    a = dict[a]
  res += a
print(res)