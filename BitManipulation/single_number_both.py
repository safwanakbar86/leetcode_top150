def singleNumber(self, nums):
    for num in nums:
        index = nums.index(num)
        if num not in nums[index+1:]:
            return num