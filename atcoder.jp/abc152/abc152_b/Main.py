a,b = map(int, input().split())
c = [str(a)*b, str(b)*a]
c.sort()
print(c[0])