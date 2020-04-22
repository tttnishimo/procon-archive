n = int(input())
s = input()
res = ''
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(s)):
  res += abc[abc.index(s[i]) + n]
print(res)