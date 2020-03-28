x,y,a,b,c = map(int, input().split())
red = sorted(list(map(int, input().split())), reverse=True)[:x]
green = sorted(list(map(int, input().split())), reverse=True)[:y]
no_c = sorted(list(map(int, input().split())), reverse=True)
print(sum(sorted(red + green + no_c, reverse=True)[:x+y]))