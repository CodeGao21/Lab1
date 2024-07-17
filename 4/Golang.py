def reverse_string(s):
    r = list(s)
    i, j = 0, len(r) - 1
    while i < j:
        r[i], r[j] = r[j], r[i]
        i += 1
        j -= 1
    return ''.join(r)

# Example usage
print(reverse_string("hello"))
