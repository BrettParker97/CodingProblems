import math

def findClosestPointsOrigin(points, k):
    ORIGIN = [0, 0]
    dists = []
    dic = {}
    #get all diststances
    #set up dict with key = dis, data = list of points(list of lists)
    for x in points:
        dis = math.dist(ORIGIN, x)
        if dis not in dists:
            dists.append(dis)
            
        try:
            dic[dis] += [x]
        except:
            dic[dis] = [x]
    
    #sort dists
    dists.sort()
    
    #start from begining and get k points from dic
    res = []
    for x in dists:
        for y in dic[x]:
            res.append(y)
            if len(res) >= k:
                return res

print (findClosestPointsOrigin([[1, 1], [3, 3], [2, 2], [4, 4], [-1, -1]], 3))
# [[-1, -1], [1, 1], [2, 2]]