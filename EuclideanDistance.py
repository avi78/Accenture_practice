import math
def calculateDist(x1,y1,x2,y2):
    return math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))

x1, y1 = map(float,input("Enter x1, y1 points: ").split())
x2, y2 = map(float,input("Enter x2, y2 points: ").split())

print(round(calculateDist(x1,y1,x2,y2),2))

# Enter x1, y1 points: 1 1
# Enter x2, y2 points: 2 4
# 3.16