class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        
        force = 0
        N = len(dominoes)
        forces = [0] * N
        for i,d in enumerate(dominoes):
            
            if d == 'R': force = N
            elif d == 'L': force = 0
            else: force = max(force -1, 0)
            forces[i] += force
            
        force = 0
        for i in range(N-1, -1, -1):
            
            if dominoes[i] == 'R': force = 0
            elif dominoes[i] == 'L': force = N
            else: force = max(force -1, 0)
            
            forces[i] -= force

        for i in range(N):
            if forces[i] == 0:
                forces[i] = '.'
            elif forces[i] < 0:
                forces[i] = 'L'
            else:
                forces[i] = 'R'

        return "".join(forces)
            