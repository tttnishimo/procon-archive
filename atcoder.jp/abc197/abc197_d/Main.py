import math
n=int(input())
a,b=map(int,input().split())
c,d=map(int,input().split())
x=(a-(a+c)/2)*math.cos(2*math.pi/n)-(b-(b+d)/2)*math.sin(2*math.pi/n)+(a+c)/2
y=(a-(a+c)/2)*math.sin(2*math.pi/n)+(b-(b+d)/2)*math.cos(2*math.pi/n)+(b+d)/2
print(x,y)