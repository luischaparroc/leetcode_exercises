

def is_subsequence(s: str, t: str) -> bool:
    if not s:
        return True

    len_s = len(s)
    index_s = 0

    for char_t in t:
        if char_t == s[index_s]:
            index_s += 1
            if index_s == len_s:
                return True

    return False
