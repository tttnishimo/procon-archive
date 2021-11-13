S=list(map(int,input()))
S.sort(reverse=True)
a='0'
b='0'
for i in range(len(S)):
  if int(a)<int(b):
    a+=str(S[i])
  else:
    b+=str(S[i])
print(int(a)*int(b))