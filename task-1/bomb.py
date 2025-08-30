import numpy as np
region = [
 [1,0,0,0,1],
 [1,0,1,1,1],
 [1,1,0,1,1],
 [1,0,1,1,0],
 [0,1,0,1,1]
]
def bestSpot(region, m):
    region = np.array(region)
    maxDamage = damage = 0
    coords = None
    n,n = np.shape(region)
    for i in range (n - m + 1): 
        damage = np.sum(region[i:i + m,0:m]) 
        fail = False or region[i + m//2, 0 + m//2] != 1
        if (maxDamage < damage and not fail): 
            maxDamage = damage 
            coords = [i,0] 
        for j in range(1, n - m + 1): 
            damage = damage - np.sum(region[i:i + m,j-1]) + np.sum(region[i:i + m,j+m-1]) 
            fail = False or region[i + m//2, j + m//2] != 1
            if (maxDamage < damage and not fail):
                maxDamage = damage 
                coords = [i,j]
    coords[0], coords[1] = coords[1] + m//2, n - 1 - (coords[0] + m//2) 
    return maxDamage, coords

def deadIslands(region, coords, m):
    region = np.array(region)
    n,n = np.shape(region)
    deadIslands = []
    tempcoords = [n - 1 - coords[1], coords[0]]
    for i in range(tempcoords[0] - m//2, tempcoords[0] + m//2 + 1):
        for j in range(tempcoords[1] - m//2, tempcoords[1] + m//2 + 1):
            if(region[i,j] == 1):
                deadIslands.append([j, n - 1 - i])
    return deadIslands

maxDamage, coords = bestSpot(region, 3)
deadIslands = deadIslands(region, coords, 3)
print(maxDamage)
print(coords)
print(deadIslands)