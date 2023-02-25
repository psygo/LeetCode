def lengthOfLongestSubstring(s):
    if s == "":
        return 0

    longest = 1

    for initIdx in range(len(s)):
        curr = s[initIdx]

        for i in range(initIdx + 1, len(s)):
            currLetter = s[i]
            if not currLetter in curr:
                curr += currLetter
            else:
                break

        if len(curr) > longest:
            longest = len(curr)

    return longest


print(lengthOfLongestSubstring("pwwkew"))
