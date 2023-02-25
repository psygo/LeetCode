def longestSubstringNoRepeatingChar(s):
    start = 0
    curr = 0
    currS = s[0]
    currLen = 1
    longestLen = 1
    posTable = {s[0]: 0}
    while curr < len(s) - 1:
        curr += 1
        currLetter = s[curr]

        if not currLetter in currS:
            print("New Letter")
            currS += currLetter
            currLen += 1
            posTable[currLetter] = curr

            if currLen > longestLen:
                longestLen = currLen
        else:
            print("Reset")
            start = posTable[currLetter] + 1
            posTable = {s[start]: start}
            curr = start
            currS = s[start]
            start = curr
            currLen = 1

    return longestLen


print(longestSubstringNoRepeatingChar("abcabcbb"))
