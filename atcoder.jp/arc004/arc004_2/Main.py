n=int(input())
a=[int(input()) for _ in range(n)]
print(sum(a))
print(max(-sum(a)+2*max(a),0))