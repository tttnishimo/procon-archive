S=input()
if 'a' not in S:
  print(-1)
else:
  print(len(S)-''.join(reversed(S)).index('a'))