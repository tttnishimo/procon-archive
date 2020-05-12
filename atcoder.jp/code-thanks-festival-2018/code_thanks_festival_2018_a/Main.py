t,a,b,c,d = map(int, input().split())
if a + c <= t:
  print(b+d)
elif a > t and c > t:
  print(0)
elif a <= t and c > t:
  print(b)
else:
  print(d)