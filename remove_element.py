def removeElement(nums, val):
    earliestValIdx = len(nums) + 1
    i = 0

    totalIter = 0

    while i < len(nums) and totalIter < 20:
        curr = nums[i]

        print("-----------------------------")
        print(i)
        print(curr)
        print(earliestValIdx)
        print(nums)
        print("-----------------------------")

        if curr == val and i < earliestValIdx:
            earliestValIdx = i
            i += 1

        elif curr != val and earliestValIdx < i:
            nums[earliestValIdx] = curr
            nums[i] = val
            i, earliestValIdx = earliestValIdx, i

        else:
            i += 1

        totalIter += 1

    nums = nums[:earliestValIdx]

    return len(nums)


print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
