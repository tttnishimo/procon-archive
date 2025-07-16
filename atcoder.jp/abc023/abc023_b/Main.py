# Check if string can be formed by pattern b->ac->ca->b expanding from center
n = int(input())
s = input()

# String must have odd length to have a center
if n % 2 == 0:
    print(-1)
else:
    valid = True
    center_pos = (n - 1) // 2
    
    # Check pattern from center outwards
    for i in range((n + 1) // 2):
        after_char = s[center_pos + i]
        before_char = s[center_pos - i]
        
        if i % 3 == 0:
            # Pattern step 0: both should be 'b'
            if after_char != 'b' or before_char != 'b':
                valid = False
        elif i % 3 == 1:
            # Pattern step 1: after='c', before='a'
            if after_char != 'c' or before_char != 'a':
                valid = False
        else:
            # Pattern step 2: after='a', before='c'
            if after_char != 'a' or before_char != 'c':
                valid = False
    
    if valid:
        print(center_pos)
    else:
        print(-1)