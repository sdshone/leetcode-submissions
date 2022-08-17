class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()
        for word in words:
            morse_word = ''.join([morse[ord(char)-ord('a')] for char in word])
            transformations.add(morse_word)
            
        print(transformations)
        return len(transformations)