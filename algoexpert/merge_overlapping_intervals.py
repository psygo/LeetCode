def mergeOverlappingIntervals(intervals):
    merged = intervals

    i = 0
    mergedLen = len(merged) - 1
    while i < mergedLen:
        curr = merged[i]
        next = merged[i + 1]

        currMax = max(curr[0], curr[1])
        nextMin = min(next[0], next[1])
        totalMin = min(curr[0], curr[1], next[0], next[1])
        totalMax = max(curr[0], curr[1], next[0], next[1])
        if nextMin <= currMax:
            merged[i] = [totalMin, totalMax]

            del merged[i + 1]
        else:
            i += 1

        mergedLen = len(merged) - 1

    return merged


print(mergeOverlappingIntervals([
    [20, 21],
    [22, 23],
    [0, 1],
    [3, 4],
    [23, 24],
    [25, 27],
    [5, 6],
    [7, 19]
]))
