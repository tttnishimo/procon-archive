a,b,c = map(int, input().split())
print(min(b,c), max(0, b + c - a))