def reverseInteger(x):
    topRange = 2**31 - 1
    bottomRange = -2**31

    currNumber = abs(x)
    numberAsList = []

    while currNumber > 0:
        rest = currNumber % 10

        numberAsList.append(rest)

        currNumber = currNumber // 10

    base = 1
    reversedNumber = 0
    for n in numberAsList[::-1]:
        reversedNumber = reversedNumber + base * n
        base *= 10

    if reversedNumber > topRange or reversedNumber < bottomRange:
        return 0
    else:
        return reversedNumber if x > 0 else -reversedNumber


print(reverseInteger(-123))
