s,t = map(str, input().split())
a,b = map(int, input().split())
u = input()
if u == s:
  a = a - 1
else:
  b = b - 1
print('{} {}'.format(a,b))