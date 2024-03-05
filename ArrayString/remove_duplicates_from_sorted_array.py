def removeDuplicates(self, nums):
    k = 0
    i = 0
    x = 1
    temp = []
    
    while i < len(nums):
        temp.append(nums[i])
        k += 1
        x = 1
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                x += 1
        i += x
        
    for i in range(k):
        nums[i] = temp[i]
        
    for i in range(len(nums) - k):
        nums.pop()