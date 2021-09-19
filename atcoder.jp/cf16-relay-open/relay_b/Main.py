S=input()
if len(S)%2:
  print('No')
  exit()
for i in range(len(S)//2):
  if (S[i]=='p' and S[-i-1]=='q') or (S[i]=='q' and S[-i-1]=='p') or (S[i]=='b' and S[-i-1]=='d') or (S[i]=='d' and S[-i-1]=='b'):
    pass
  else:
    print('No')
    exit()
print('Yes')