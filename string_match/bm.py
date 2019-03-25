from typing import List

SIZE = 256  # charset capacity


def generate_bad_char_table(pattern):
    bc = [-1] * SIZE
    for i, c in enumerate(pattern):
        bc[ord(c)] = i
    return bc


def generate_good_suffix_table(pattern):
    m = len(pattern)
    prefix, suffix = [False] * m, [-1] * m  # index -- suffix length
    for i in range(m - 1):  # end index of substring
        j = i  # compare position of suffix, compare from back to front
        k = 0  # length of common suffix
        while j >= 0 and pattern[j] == pattern[~k]:  # use '~' to get k-th to last
            j -= 1
            k += 1
            suffix[k] = j + 1  # overwrite previous data, store match suffix index
        if j == -1:
            prefix[k] = True
    return prefix, suffix


def move_by_good_suffix(bc_index, suffix, prefix):  # type: (int, List[int], List[bool]) -> int
    """
    calculate pattern move distance by taking good_suffix rule
    :param bc_index:
    :param suffix:
    :param prefix:
    """
    k = len(suffix) - 1 - bc_index  # remaining pattern string length
    if k <= 0:  # return if not have suffix
        return 0
    if suffix[k] != -1:  # suffix match exist
        return bc_index - suffix[k] + 1
    for r, match_pre in enumerate(reversed(prefix[:k]), bc_index + 2):
        if match_pre:
            return r
    return len(suffix)


def bm(s, pattern):
    bc = generate_bad_char_table(pattern)
    prefix, suffix = generate_good_suffix_table(pattern)
    n, m = len(s), len(pattern)
    i = 0  # string index
    while i <= n - m:  # use "while" instead of "for" because i may increase multiple
        j = m - 1  # pattern index, compare from back to front
        while j >= 0:
            if s[i + j] != pattern[j]:  # s[i + j] is bad character
                break
            j -= 1
        if j < 0:
            return i
        x = j - bc[ord(s[i + j])]  # bad character rule shift distance
        y = move_by_good_suffix(j, suffix, prefix)  # good suffix rule shift distance
        i += max(x, y)
    return -1


if __name__ == "__main__":
    s = "Here is a simple example"
    pattern = "example"
    print(bm(s, pattern))

    s = "abcdcccdc"
    pattern = "cccd"
    print(s.find(pattern) == bm(s, pattern))
