def romanToInt(s: str):
    currentTotal = 0
    table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    pt = len(s) - 1

    while pt >= 0:
        currentLetter = s[pt]
        currentTotal += table[currentLetter]

        next = s[pt - 1] if pt > 0 else ""

        if next == "I" and (currentLetter == "V" or currentLetter == "X"):
            currentTotal -= 1
            pt -= 1
        elif next == "X" and (currentLetter == "L" or currentLetter == "C"):
            currentTotal -= 10
            pt -= 1
        elif next == "C" and (currentLetter == "D" or currentLetter == "M"):
            currentTotal -= 100
            pt -= 1

        pt -= 1
        
        print("------------------------------------------")
        print(currentTotal)
        print(next)
        print("------------------------------------------")

    return currentTotal


print(romanToInt("MMMCDXC"))
