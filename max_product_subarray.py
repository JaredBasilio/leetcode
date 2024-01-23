def maximumProductSubarray(nums):
    # O(n)/O(1) : Time/Memory

    # maintain a running minimum and maximum, for each iteration, compare this running max to the newProduct of n * curMax, n * curMin, and n
    
    # sample iteration
    # currMin currMax res
    # 2       2       2
    # 2       6       6
    # -12     -2      6
    # -24       4      6

    # we keep the current min because if we see another negative we can consider it
    # if n > currMax, this becomes are new starting point for an array

    res = nums[0]
    curMin, curMax = 1, 1

    for n in nums:

        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)
    return res


nums = [2,3,-2,4]
print("Input:", nums)
print("Expected:", 6)
print("Received:", maximumProductSubarray(nums))

nums = [-2, 0, -1]
print("Input:", nums)
print("Expected:", 0)
print("Received:", maximumProductSubarray(nums))