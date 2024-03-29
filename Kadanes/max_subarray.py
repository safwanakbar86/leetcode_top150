def maxSubArray(self, nums):
    memo = [nums[0]]
    for i in range(1, len(nums)):
        memo.append(max(memo[i-1] + nums[i], nums[i]))
    return max(memo)
