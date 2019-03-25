def get_next(pattern):
    m = len(pattern)
    next_index = [-1] * m
    k = -1  # [next_index]'s value -- matched prefix index
    for i in range(1, m):  # [next_index]'s index -- prefix end index
        while k != -1 and pattern[k + 1] != pattern[i]:
            k = next_index[k]  # second-longest match sub-prefix end index
        if pattern[k + 1] == pattern[i]:
            k += 1
        next_index[i] = k
    return next_index


def kmp(s, pattern):
    n, m = len(s), len(pattern)
    if m == 0:
        return 0
    if n <= m:
        return 0 if s == pattern else -1
    next_index = get_next(pattern)
    j = 0  # pattern index
    for i in range(n):  # string index
        while j > 0 and s[i] != pattern[j]:
            j = next_index[j - 1] + 1  # switch to next position of previous prefix
        if s[i] == pattern[j]:  # break loop because match, j jump to next position
            j += 1
        if j == m:  # j arrive pattern end
            return i - (m - 1)
    return -1


if __name__ == '__main__':
    s = "abc abcdab abcdabcbcdabcbcdbde"
    pattern = "bcdabcbcd"
    print(kmp(s, pattern), s.find(pattern))

    # s = "hello"
    # pattern = "ll"
    # print(kmp(s, pattern), s.find(pattern))
