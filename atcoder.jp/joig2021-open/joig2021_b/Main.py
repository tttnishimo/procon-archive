N,K=map(int,input().split())
T=input()
S=''
for i in range(N):
  if i>=K-1:
    if T[i].islower():
      S+=T[i].upper()
    else:
      S+=T[i].lower()
  else:
    S+=T[i]
print(S)