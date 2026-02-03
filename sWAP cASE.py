def swap_case(s):
    t = ''
    for c in s:
        if c.isalpha():
            t += c.lower() if c == c.upper() else c.upper()
        else: t += c
    return t

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
