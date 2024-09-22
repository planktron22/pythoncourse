def length_of_longest_substring(s: str) -> int:
    start = 0  
    ml = 0  
    used_chars = {}   
    for i, ch in enumerate(s):
        if ch in used_chars and start <= used_chars[ch]:
            start = used_chars[ch] + 1       
        used_chars[ch] = i       
        ml = max(ml, i - start + 1)  
    return ml

s = str(input())
print(length_of_longest_substring(s))  
    
        
    
        

