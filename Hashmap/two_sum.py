# BRUTE FORCE APPROACH O(N^2)
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

# HASHMAP APPROACH O(N)
    def twoSum(self, nums, target):
        return_list = []
        c = 1
        
        for n in range(len(nums) - 1):
            temp_nums = nums[n+1:]
            if target - nums[n] in temp_nums:
                return_list.append(n)
                return_list.append(temp_nums.index(target - nums[n]) + c)
            c += 1
        
        return return_list

# COMPRESSED HASHMAP APPROACH O(N)
    def twoSum(self, nums, target):
        for n in range(len(nums) - 1):
            if (target - nums[n]) in nums[n+1:]:
                return [n, nums[n+1:].index(target - nums[n]) + (n+1)]
                
