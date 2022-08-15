class Solution:
    def numDecodings(self, s: str) -> int:
        
        mapping = {}
        for i in range(1,27):
            mapping[i] = True
        print(mapping)

        count = {len(s):1}
        for i in range(len(s)-1,-1,-1):
            if mapping.get(int(s[i])):
                count[i] = count[i+1]
                if i+1 < len(s) and mapping.get(int(s[i:i+2])):
                    count[i]+=count[i+2]
            else:
                count[i]=0
            print(count, s[i:i+2])
                
        return count[0]
            