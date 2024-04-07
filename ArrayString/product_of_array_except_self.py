  def productExceptSelf(self, nums):
      length = len(nums)
      result = 1
      answer =[1] * length
      
      for index in range(length):
          answer[index] = result
          result *= nums[index]
          
      result = 1
      for index in reversed(range(length)):
          answer[index] *= result
          result *= nums[index]
          
      return answer
