L,R=map(int,input().split())
S=input()
print(S[:L-1]+''.join(reversed(S[L-1:R]))+S[R:])