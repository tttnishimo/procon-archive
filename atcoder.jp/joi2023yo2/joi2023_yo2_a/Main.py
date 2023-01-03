N=int(input())
A=list(map(int,input().split()))
A_M=max(A)
A_m=min(A)
for a in A:
  print(max(abs(A_M-a),abs(A_m-a)))