def maxele():
    l = [2, 6, 8, 11, 4]
    max_val = l[0]
    for i in l:
        if i > max_val:
            max_val = i
    return max_val
print(maxele())
