class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n
        ugly_numbers[0] = 1  
        index2, index3, index5 = 0, 0, 0
        next2, next3, next5 = 2, 3, 5
        
        for i in range(1, n):
            next_ugly = min(next2, next3, next5)
            ugly_numbers[i] = next_ugly
            
            if next_ugly == next2:
                index2 += 1
                next2 = ugly_numbers[index2] * 2
            if next_ugly == next3:
                index3 += 1
                next3 = ugly_numbers[index3] * 3
            if next_ugly == next5:
                index5 += 1
                next5 = ugly_numbers[index5] * 5
        
        return ugly_numbers[-1]  

sol = Solution()
n = int(input())  
print(sol.nthUglyNumber(n))
