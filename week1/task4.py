from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []       
        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        def gen(index: int, path: str):
            if len(path) == len(digits):
                combo.append(path)
                return
            
            possible_letters = digit_to_char[digits[index]]
            for letter in possible_letters:
                gen(index + 1, path + letter)

        combo = []
        gen(0, "")
        
        return combo

sol = Solution()
digits = input()
print(sol.letterCombinations(digits))
