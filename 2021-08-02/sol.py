
class LRUCache:
    def __init__(self, listSize):
        self.listSize = listSize
        self.FIFO = []
        self.cache = {}
        
    def addToFIFO(self, value):
        res = None
        #if value is in list, then delete it
        #and bring it to the front
        if value in self.FIFO:
            self.FIFO.remove(value)
            self.FIFO = [value] + self.FIFO
        #if its not at front of list, check size of list
        else:
            #if list is max size, pop something
            if len(self.FIFO) >= self.listSize:
                res = self.FIFO[len(self.FIFO) - 1]
                self.FIFO.pop()
                self.FIFO = [value] + self.FIFO
            #if list isnt max size, just place value at front
            else:
                self.FIFO = [value] + self.FIFO
        return res

    def get(self, key):
        #check cache for value, if its not in there
        #then dont bother adding it to FIFO
        res = None
        try:
            res = self.cache[key]
        except KeyError:
            res = None
        
        if res == None:
            return None
            
        #update FIFO, we dont care if something is poped here
        self.addToFIFO(key)
        
        #return whats in the dictionary
        return res
        
    def put(self, key, value):
        #check FIFO, if something is poped then del
        #from the cache as well
        res = self.addToFIFO(key)
        if res != None:
            del self.cache[res]
        
        #add to cache and return
        self.cache[key] = value

cache = LRUCache(2)

cache.put(3, 3)
cache.put(4, 4)
print(cache.get(3))
# 3
print(cache.get(2))
# None

cache.put(2, 2)

print(cache.get(4))
# None (pre-empted by 2)
print(cache.get(3))
# 3