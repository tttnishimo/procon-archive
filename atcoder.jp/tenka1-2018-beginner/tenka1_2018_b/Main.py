a,b,k = map(int, input().split())
for i in range(k):
  if i % 2 == 0:
    a = a // 2
    b = b + a
  else:
    b = b // 2    
    a = a + b
print(a,b)
