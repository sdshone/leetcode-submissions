class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        return ' '.join([word[::-1] for word in s.split(' ')])
        
#         words = []
#         idx_s = 0
#         for idx_e, char in enumerate(s):
            
#             if char == ' ':
#                 words.append(s[idx_s: idx_e])
#                 idx_s = idx_e+1
#             if idx_e == len(s)-1:
#                 words.append(s[idx_s: idx_e+1])
                
                
#         # print(words)
        
#         for idx,word in enumerate(words):
            
#             words[idx] = word[::-1]
            
#         # print(words)
        
#         return ' '.join(words)