#!/usr/bin/env python3

# Tried memoization but the printing process couldn't be matched to the tests. 
# Instead I stuck to the loop approach
def print_fibonacci(length):

    seq = []
    if length > 0 :
        for i in range(length):
            if i == 0:
                seq.append(0)
            elif i == 1:
                seq.append(1)
            else:
                try:
                    seq.append((seq[i - 1] + seq[i-2]))
                except IndexError: 
                    print("Out of bounds")
    print(seq)

'''
Memoization Code: 

def print_fibonacci(length, memo={}, top_level=True):
    if length <= 1:
        return length
    elif length not in memo:
        # Recursive calls without printing
        memo[length] = print_fibonacci(length - 1, memo, top_level=False) + print_fibonacci(length - 2, memo, top_level=False)

        # Print values only at the top level
        if top_level:
            print(list(memo.values()))

    return memo[length]

'''
print_fibonacci(0)
