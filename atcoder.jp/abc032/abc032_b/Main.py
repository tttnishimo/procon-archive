s = input()
k = int(input())
tmp = []
if k > len(s):
  print(0)
else:
  i = 0
  while i+k in range(len(s)+1):
    tmp.append(s[i:i+k])
    i = i + 1
  print(len(list(set(tmp))))