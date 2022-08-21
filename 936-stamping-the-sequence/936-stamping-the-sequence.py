class Solution:
    
    def equals(self, idx, stamp, target):
        
        for i, char in enumerate(stamp):
            target_char = target[idx+i]
            if not (target_char == char or target_char == '?'):
                return False
        return True
    
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        
        T_LEN, S_LEN = len(target), len(stamp)
        
        res = []
        seen = set()
        
        for i in range(T_LEN - S_LEN + 1):
            
            if self.equals(i, stamp, target):
                
                for j in range(i, -1, -1):
                    
                    if j in seen:
                        break
                    seen.add(j)
                    if self.equals(j, stamp, target):
                        res.append(j)
                        # target[j:j+S_LEN] = '?'*M
                        target = f'{target[:j]}'+f'{"?"*S_LEN}'+f'{target[j+S_LEN:]}'
                        print(target)
        
        return res[::-1] if target == '?'*T_LEN else []
                        
        
        