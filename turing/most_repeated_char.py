# O(n) T | O(k) S, k size of alphabet
def mostRepeatedChar(s):
    table = {}

    for l in s:
        if l in table:
            table[l] += 1
        else:
            table[l] = 1

    return max(table, key=table.get)


print(mostRepeatedChar("abcddefda111l33333333333333333"))
