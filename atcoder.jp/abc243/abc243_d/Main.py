N,X=map(int,input().split())
X=list(bin(X))
S=input()
for s in S:
  if s=='U':
    X.pop()
  elif s=='L':
    X.append("0")
  else:
    X.append("1")
print(int("".join(X),2))