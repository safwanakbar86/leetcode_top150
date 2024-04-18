def findPeakElement(self, nums):
    if len(nums) < 3:
        return nums.index(max(nums))
    
    else:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    left = mid + 1
            
            elif mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    right = mid - 1
                
            else:
                if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    return mid
                elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                    left = mid + 1
                elif nums[mid] < nums[mid - 1] and nums[mid] > nums[mid + 1]:
                    right = mid - 1
                else:
                    left = mid + 1
