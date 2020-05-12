s = input()
al = 'ABCDEF'
a = [0,0,0,0,0,0]
for i in range(len(s)):
  a[al.index(s[i])] += 1
print(*a)