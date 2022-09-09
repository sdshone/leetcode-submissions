class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
#         attack_dict = defaultdict(list)
#         for a,d in properties:
#             attack_dict[a].append(d)
            
#         attacks = sorted(attack_dict.keys())
#         # print(attack_dict)
#         # print(attacks)
        
#         max_d = [max(attack_dict[a]) for a in attacks]
        
#         # print(max_d)
#         res = 0
#         for i in range(len(attacks)):
#             if max_d[i+1:] and max_d[i] < max(max_d[i+1:]):
#                 res+=len(attack_dict[attacks[i]])
#             else:
#                 for d in attack_dict[attacks[i]]:
#                     if max_d[i+1:] and d < max(max_d[i+1:]):
#                         res+=1
                
#         return res

        properties.sort(key=lambda p: (-p[0], p[1]))
        print(properties)
        count = 0
        maxa = properties[0][0]
        maxd = properties[0][1]

        for a, d in properties:
            if a < maxa and d < maxd:
                count+=1
            else:
                maxa=a
                maxd=d
        return count
