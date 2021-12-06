N=input()
if int(N)>41:
  print('AGC0'+str(int(N)+1))
else:
  print('AGC0'+'0'*(2-len(N))+N)