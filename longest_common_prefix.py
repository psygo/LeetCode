def longestCommonPrefix(strs) -> str:
    common = ""
    currentLetter = ""
    idx = 0

    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]

    while True:
        for w in strs:
            if len(w) == 0:
                return ""

            if len(w) == idx:
                return common

            if currentLetter == "":
                currentLetter = w[idx]

            if currentLetter != w[idx]:
                return common

        common += currentLetter
        idx += 1
        currentLetter = ""


print(longestCommonPrefix(["ab", "a"]))
