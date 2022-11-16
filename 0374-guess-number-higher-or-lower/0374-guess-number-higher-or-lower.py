# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        s = 1
        while True:
            guess_num = (s + n) // 2
            
            if guess(guess_num) == -1:
                n = guess_num-1
            elif guess(guess_num) == 1:
                s = guess_num+1
            else:
                return guess_num