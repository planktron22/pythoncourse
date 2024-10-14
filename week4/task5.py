from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        nums_str.sort(key=cmp_to_key(compare))
        largest_number = ''.join(nums_str)
        if largest_number[0] == '0':
            return '0'
        return largest_number

nums_input = input()
nums = eval(nums_input)
solution = Solution()
result = solution.largestNumber(nums)
print(result)
