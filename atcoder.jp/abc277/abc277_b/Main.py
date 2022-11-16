N=int(input())
A=[input() for _ in range(N)]
b=['S','H','D','C']
c=['A','2','3','4','5','6','7','8','9','T','J','Q','K']
if N!=len(set(A)):
  print('No')
  exit()
for a in A:
  if a[0] in b and a[1] in c:
    continue
  else:
    print('No')
    exit()
print('Yes')