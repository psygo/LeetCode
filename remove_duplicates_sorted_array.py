def removeDuplicates(nums):
    seen = {}
    repeatQ = []

    for i in range(len(nums)):
        curr = nums[i]

        if not curr in seen:
            if len(repeatQ) != 0:
                nums[repeatQ[0]] = curr
                repeatQ.pop(0)
                repeatQ.append(i)

            seen[curr] = i

        else:
            repeatQ.append(i)

    nums = nums[:len(seen)]

    return nums


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
