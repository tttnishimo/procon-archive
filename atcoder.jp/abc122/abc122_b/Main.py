s = input()
acgt = ['A', 'C', 'G', 'T']
if s[0] in acgt:
  tmp = 1
else:
  tmp = 0
res = tmp
for i in range(len(s)-1):
  if s[i+1] in acgt:
    tmp += 1
    res = max(res, tmp)
  else:
    tmp = 0
print(res)