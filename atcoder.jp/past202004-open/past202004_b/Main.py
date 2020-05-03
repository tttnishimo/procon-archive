s = input()
a = [0,0,0]
for i in range(len(s)):
  if s[i] == 'a':
    a[0] += 1
  elif s[i] == 'b':
    a[1] += 1
  else:
    a[2] += 1
s = 'abc'
print(s[a.index(max(a))])