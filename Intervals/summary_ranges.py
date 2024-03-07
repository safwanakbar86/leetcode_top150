def summaryRanges(self, nums):
  if len(nums) == 0:
      return ""
  
  str_list = []
  return_str = ""
  interval_flag = False
  
  for num in range(1, len(nums)):
      if nums[num] - nums[num - 1] == 1 and interval_flag == False:
          return_str = return_str + str(nums[num - 1]) + "->"
          interval_flag = True
          
      elif nums[num] - nums[num - 1] > 1:
          return_str += str(nums[num - 1])
          str_list.append(return_str)
          return_str = ""
          if interval_flag == True:
              interval_flag = False
  
  return_str += str(nums[-1])
  str_list.append(return_str)
  return str_list
