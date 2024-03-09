#INCOMPLETE
#BRUTE FORCE APPROACH COMPLETE

def threeSum(self, nums):
        nums = sorted(nums)
        answer = []
        for x in range(len(nums) - 2):
            for y in range(x + 1, len(nums) - 1):
                for z in range(y + 1, len(nums)):
                    if nums[x] + nums[y] + nums[z] == 0 and [nums[x], nums[y], nums[z]] not in answer:
                        answer.append([nums[x], nums[y], nums[z]])
        return answer
