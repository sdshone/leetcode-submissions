class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        
        guess_count = collections.Counter(guess)
        secret_count = collections.Counter(secret)
        
        # Find bulls
        bulls = 0
        cows = 0
        done_set = set()
        for idx in range(len(guess)):
            if guess[idx] == secret[idx]:
                bulls += 1
            if secret_count[guess[idx]] and guess[idx] not in done_set:
                done_set.add(guess[idx])
                cows +=min(secret_count[guess[idx]], guess_count[guess[idx]])
        
        cows -= bulls
        cows = 0 if cows < 0 else cows
        return f'{bulls}A{cows}B'
        
        