n = int(input())
s = input()
res = [0]
for i in range(n):
  if s[i] == 'I':
    res.append(res[-1]+1)
  else:
    res.append(res[-1]-1)
print(max(res))