def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1

    ans = 0

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] < target:
            start = mid + 1
            ans = mid + 1

        elif nums[mid] > target:
            end = mid - 1

        else:
            return mid

    return ans


print(searchInsert([1, 3, 5, 6], 2))
