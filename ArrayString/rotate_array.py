def rotate(self, nums, k):
    def reverse(nums, i, j):
        while i < j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1

    k = k % len(nums)
    reverse(nums, 0, len(nums) - k - 1)
    reverse(nums, len(nums) - k, len(nums) - 1)
    reverse(nums, 0, len(nums) - 1)