class Solution:
    def build(self, wordList):
        self.wordList = wordList
    
    def autocomplete(self, word):
        wordLen = len(word)
        res = []
        #loop through all words in word list O(n)
        for x in self.wordList:
            #x[:wordLen] would be O(k) where k is size of word
            # x == y is O(1)
            #append = O(1)
            if word == x[:wordLen]:
                res.append(x)
        
        #result is O(nk + 2) upperbound or O(n)
        #therefor linear time
        return res

s = Solution()
s.build(['dog', 'dark', 'cat', 'door', 'dodge'])
print(s.autocomplete('do'))
# ['dog', 'door', 'dodge']