from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  
        n = len(nums)
        res = []  
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  
                    continue
                
                left, right = j + 1, n - 1  
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum < target:
                        left += 1
                    elif current_sum > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1                      
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        
        return res

arr = input()
nums = list(map(int, arr.strip('[]').split(',')))
target = int(input())
solution = Solution()
result = solution.fourSum(nums, target)
fres = '[' + ','.join('[' + ','.join(map(str, quadruplet)) + ']' for quadruplet in result) + ']'   
print(fres)
