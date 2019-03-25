from time import time


def bf(string, pattern):
    n = len(string)
    m = len(pattern)
    if n <= m:  # pattern is long
        return 0 if pattern == string else -1
    for i in range(n - m + 1):  # total count of possible substring: [n-m+1]
        for j in range(m):
            if string[i + j] == pattern[j]:
                if j == m - 1:  # achieve the end point: [m-1]
                    return i
                else:
                    continue
            else:
                break  # meet mismatch, break
    return -1


def simple_hash(s, start, end):
    """
    calculate hash value as sum of hex
    :param s: string that ready to compare
    :param start: start index(include)
    :param end: end index(exclude)
    :return: hash value
    """
    assert start <= end
    ret = 0
    for c in s[start:end]:
        ret += ord(c)
    return ret


def simple_hash_recursive(head_char, tail_char, prev_hash):
    """
    calculate hash value by using previous hash value
    :param head_char: char that will be discard
    :param tail_char: char that will be adjunct
    :param prev_hash: previous hash value
    :return:
    """
    return prev_hash - ord(head_char) + ord(tail_char)


def simple_hash_compare(hash_string, hash_pattern, string, pattern):
    """
    hash value comparision, need to compare origin string to avoid hash collision
    :param hash_string:
    :param hash_pattern:
    :param string:
    :param pattern:
    :return:
    """
    if hash_string == hash_pattern:
        if string == pattern:
            return True
        else:
            return False
    else:
        return False


def rk(string, pattern):
    n = len(string)
    m = len(pattern)
    if n <= m:
        return 0 if pattern == string else -1
    hash_string = simple_hash(string, 0, m)
    hash_pattern = simple_hash(pattern, 0, m)
    if simple_hash_compare(hash_string, hash_pattern, string[0:m], pattern):
        return 0
    for i in range(1, n - m + 1):
        # update hash value
        hash_string = simple_hash_recursive(string[i - 1], string[i + m - 1], hash_string)
        if simple_hash_compare(hash_string, hash_pattern, string[i:i + m], pattern):
            return i
    return -1


if __name__ == '__main__':
    m_str = 'a' * 10000
    p_str = 'a' * 200 + 'b'

    print('---time consume---')
    t = time()
    print('[bf] result:', bf(m_str, p_str))
    print('[bf] time cost: {0:.5}s'.format(time() - t))

    t = time()
    print('[rk] result:', rk(m_str, p_str))
    print('[rk] time cost: {0:.5}s'.format(time() - t))

    print('--- search ---')
    m_str = 'thequickbrownfoxjumpsoverthelazydog'
    p_str = 'ydog'
    print('[bf] result:', bf(m_str, p_str))
    print('[rk] result:', rk(m_str, p_str))
