def pallindrome_tuple(tup):
    e = len(tup)-1
    s = 0
    while s < e:
        if tup[s] != tup[e]:
            return False
        s += 1
        e -= 1
    return True
sample_tuple = (1, 2, 3, 2, 1)
if pallindrome_tuple(sample_tuple):
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")