

def is_isomorphic(s: str, t: str) -> bool:
    chars_mapper_s = {}
    chars_mapper_t = {}

    for char_s, char_t in zip(s, t):
        if not chars_mapper_s.get(char_s):
            chars_mapper_s[char_s] = char_t
        elif chars_mapper_s[char_s] != char_t:
            return False

        if not chars_mapper_t.get(char_t):
            chars_mapper_t[char_t] = char_s
        elif chars_mapper_t[char_t] != char_s:
            return False

    return True
