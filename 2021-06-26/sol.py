import math

def closest_points(points, k):
    res = []
    dists = []
    for p in points:
        x = p[0] * p[0]
        y = p[1] * p[1]
        
        aMax = max(dists)
        aLen = len(dists)
        dist = math.sqrt(x + y)
        #repalce distance with new point and distance
        if aLen < k:
            res.append(p)
            dists.append(dist)
        elif dist < aMax and aLen == k:
            #remove old
            index = dists.index(aMax)
            del dists[index]
            del res[index]
            
            #place new
            res.append(p)
            dists.append(dist)
    return res

print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))
# [(1, 2), (0, 0)]
