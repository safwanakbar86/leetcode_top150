def searchRange(self, nums, target):     
    if nums == []:
        return [-1, -1]
    
    else:
        if target not in nums:
            return [-1, -1]
        
        else:
            left = nums.index(target)
            positions = [left]
            
            left += 1
            right = len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] == target:
                    left = mid + 1
                    
            positions.append(right)
            return positions
