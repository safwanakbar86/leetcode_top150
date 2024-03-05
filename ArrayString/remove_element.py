def removeElement(self, nums, val):
    k = 0
    x = 0
    temp = []
    
    for i in range(len(nums)):
        if nums[i] != val:
            temp.append(nums[i])
            k += 1
        else:
            x += 1
            
    for i in range(k):
        nums[i] = temp[i]
    
    for i in range(x):
        nums.pop()
        
    return k