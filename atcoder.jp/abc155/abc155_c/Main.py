n = int(input())
d = {}
for i in range(n):
  s = input()
  if s in d:
    d[s] += 1
  else:
    d[s] = 1
max_d = max(d.values())
d = sorted(d.items(), key = lambda x : x[0])
for i in range(len(d)):
  if d[i][1] == max_d:
    print(d[i][0])