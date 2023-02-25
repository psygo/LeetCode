def longestPeak(array):
    if len(array) == 0:
        return 0

    maxPeak = 0
    ascent = [array[0]]
    descent = []

    for i in range(1, len(array)):
        curr = array[i]
        prev = array[i - 1]

        if curr > prev and len(descent) == 0:
            ascent.append(curr)
        elif curr < prev and len(ascent) > 0:
            descent.append(curr)
        else:
            ascent = [prev, curr] if curr > prev else (
                [curr] if curr == prev else [])
            descent = []

        ascentLen, descentLen = len(ascent), len(descent)
        totalLen = ascentLen + descentLen
        if totalLen > maxPeak and totalLen >= 3 and len(ascent) >= 2 and len(descent) >= 1:
            maxPeak = totalLen

    return maxPeak


print(longestPeak([1, 1, 3, 2, 1]))
