def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    map_st = {}
    map_ts = {}

    for i in range(len(s)):
        c1 = s[i] # karakter di string s
        c2 = t[i] # karakter di string t

        if c1 in map_st:
            if map_st[c1] != c2:
                return False
        else:
            map_st[c1] = c2

        if c2 in map_ts:
            if map_ts[c2] != c1:
                return False
        else:
            map_ts[c2] = c1

    return True

s = input()
t = input()

# print(is_isomorphic(s, t))
if is_isomorphic(s, t):
    print('true')
else:
    print('false')