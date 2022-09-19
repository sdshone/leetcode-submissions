class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        
        res = defaultdict(list)
        for path in paths:
            
            files = path.split(" ")
            dir_name = files[0]
            files = files[1:]
            for file in files:
                
                name = file.split("(")
                content = name[1]
                name = name[0]

                res[content].append(f'{dir_name}/{name}')
                                    
        ret = []
        
        for key in res.keys():
            if len(res[key])>1:
                ret.append(res[key])
        return ret