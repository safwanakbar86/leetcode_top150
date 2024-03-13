def removeDuplicates(self, nums):
        k = len(nums)
        c = 1
        n = 1

        while n < k:
            if nums[n] == nums[n-1] and c != 2:
                c += 1
                n += 1
            elif nums[n] == nums[n-1] and c == 2:
                k -= 1
                nums.append(nums.pop(n))
            else:
                c = 1
                n += 1
        return k
