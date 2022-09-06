S=input()
A=S[6]+S[3]+str(int(S[1]) or int(S[7]))+str(int(S[0]) or int(S[4]))+str(int(S[2]) or int(S[8]))+S[5]+S[9]
a=['101','1001','10001','100001','1000001']
if S[0]=='0':
  for i in a:
    if i in A:
      print('Yes')
      exit()
  print('No')
else:
  print('No')