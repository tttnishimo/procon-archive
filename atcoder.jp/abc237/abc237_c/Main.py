S=input()
T=S
a_f=0
a_b=0
for i in range(len(S)):
  if S[-i-1]=='a':
    a_b+=1
  else:
    break
for i in range(len(S)-a_b):
  if S[i]=='a':
    a_f+=1
  else:
    break
if a_b==0:
  S=T[a_f:]
else:
  S=T[a_f:-a_b]
for i in range(len(S)//2):
  if S[i]!=S[-i-1]:
    print('No')
    exit()
if a_b>=a_f:
  print('Yes')
else:
  print('No')