class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        q = deque() 
        for char in s:
            if q and q[-1] == char:
                q.pop()
            else:
                q.append(char)
        return ''.join(q)
        
        
#         changed = True
#         while changed:
#             new_s = ''
#             i=0
#             while i <(len(s)-1):
#                 # print(s[i], s[i+1])
#                 if s[i] !=s[i+1]:
#                     new_s += s[i]
#                     i+=1
#                 else:
#                     i+=2
#                 # print(new_s)
#             # if i == len(s)-1:
#             new_s+=s[i]
#             # print(new_s)
#             changed = new_s != s
#             s = new_s
#             # print(s, changed)
            
#         return new_s