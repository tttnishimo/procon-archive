n=str(bin(int(input())))[2:]
flg=0
for i in range(len(n)):
  if n[i]!=n[-i-1]:
    flg=1
if flg==0:
  print('Yes')
else:
  print('No')