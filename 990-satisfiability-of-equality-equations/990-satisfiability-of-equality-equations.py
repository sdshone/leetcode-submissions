class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        
        unionfind = {}
        
        def find(x):
            
            unionfind.setdefault(x,x)
            if x != unionfind[x]:
                unionfind[x] = find(unionfind[x])
            return unionfind[x]        
        
        def union(x,y):
            
            unionfind[find(x)] = find(y)
            
        for e in equations:
            
            if e[1] == '=':
                union(e[0], e[-1])
        for e in equations:
            
            if e[1] == '!' and find(e[0]) == find(e[-1]):
                return False
        return True
                