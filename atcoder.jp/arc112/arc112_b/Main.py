B,C=map(int,input().split())
a=B-C//2
b=max(B+C//2-1,B)
c=-B-(C-1)//2
d=-B+(C-1)//2
print((b-a+1)+(d-c+1)-max(0,min(b,d)-max(a,c)+1))