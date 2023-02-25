def lengthOfLastWord(s):
    split = s.split(" ")

    filtered = list(filter(lambda w: True if w != "" else False, split))

    print(filtered)

    return filtered[-1]


print(lengthOfLastWord("   fly me   to   the moon  "))
