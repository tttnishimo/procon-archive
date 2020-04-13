a,b = map(str, input().split())
a = int(a+b)
b = 'No'
for i in range(1, int(pow(a,1/2) + 1)):
  if i ** 2 == a:
    b = 'Yes'
print(b)