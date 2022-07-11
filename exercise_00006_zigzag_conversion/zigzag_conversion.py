

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    zigzag_list = ["" for _ in range(numRows)]

    index_s = 0
    index_j = 0

    while index_s < len(s):

        if index_j == 0:
            substring = s[index_s: index_s + numRows]

            for i, char in enumerate(substring):
                zigzag_list[i] += char

            index_s += numRows

        else:
            zigzag_list[numRows - 1 - index_j] += s[index_s]
            index_s += 1

        index_j += 1
        index_j %= numRows - 1

    zigzag_string = ''.join(zigzag_list)

    return zigzag_string
