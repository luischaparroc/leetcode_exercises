

def lengthOfLongestSubstring(s: str) -> int:
    indexes = {}
    max_length = 0
    tmp_s = ""

    for index, letter in enumerate(s):

        if letter in tmp_s:
            len_string = len(tmp_s)

            if len_string > max_length:
                max_length = len_string

            slice_from = indexes[letter]
            tmp_s = s[slice_from + 1: index + 1]

        else:
            tmp_s += letter

        indexes[letter] = index

    len_string = len(tmp_s)

    if len_string > max_length:
        max_length = len_string

    return max_length
