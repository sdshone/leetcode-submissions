class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        players = {}
        all_players = set()
        for match in matches:
            if players.get(match[1]):
                players[match[1]] += 1
            else:
                players[match[1]] = 1
            all_players.add(match[0])
            all_players.add(match[1])
            
        res = []
        res.append(sorted(list(all_players - set(players.keys()))))
        one_count = {p for p, c in players.items() if c== 1 }
        res.append(sorted(list(one_count)))
        return res