a = input()
b = input()
s = ""
for i in range(len(b)):
  s = s + a[i]
  s = s + b[i]
if len(a) != len(b):
  s = s + a[len(a)-1]
print(s)