#runtime analysis= 
#   dict set up = O(n) *where n is size of magazine
#   3 operations per note char = O(1)
#   Overall runtime = O(n) or linear
class Solution(object):
  def canSpell(self, magazine, note):
    #set up dictionary for that sweet O(1)
    #runtime
    dic = {}
    for x in magazine:
        try:
            dic[x] = dic[x] + 1
        except:
            dic[x] = 1
    
    #check the note letters
    for x in note:
        try:
            #try to get value out of dict
            temp = dic[x]
            
            #if theres only 1 occurance then delete
            #value from dict
            if temp - 1 == 0:
                del dic[x]
            else:
                dic[x] = dic[x] - 1
        except:
            return False
    return True
    
print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
# True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'cat'))
# False