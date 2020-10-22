sx,sy,tx,ty=map(int,input().split())
a=tx-sx
b=ty-sy
print('R'*a+'U'*b+'L'*a+'D'*b+'D'+'R'*(a+1)+'U'*(b+1)+'L'+'U'+'L'*(a+1)+'D'*(b+1)+'R')