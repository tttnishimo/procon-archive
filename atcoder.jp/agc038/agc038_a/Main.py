h,w,a,b=map(int,input().split())
print(*['0'*a+'1'*(w-a) if i>=b else '1'*a+'0'*(w-a) for i in range(h)],sep='\n')