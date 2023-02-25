def twoSum(nums, target):
    numsTable = {}

    for i in range(len(nums)):
        num = nums[i]
        potentialMatch = target - num

        if potentialMatch in numsTable:
            return [numsTable[potentialMatch], i]
        else:
            numsTable[num] = i

    return []

# def twoSumAttempt(nums, target):
#     sortedNums = sorted(nums)

#     leftPt = 0
#     rightPt = len(nums) - 1

#     while leftPt < rightPt and leftPt != rightPt:
#         left = sortedNums[leftPt]
#         right = sortedNums[rightPt]
#         sum = left + right

#         if sum < target:
#             leftPt += 1
#         elif sum > target:
#             rightPt -= 1
#         else:
#             return [nums.index(left), nums.index(right)]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
