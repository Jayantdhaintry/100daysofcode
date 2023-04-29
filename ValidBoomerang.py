def isBoomerang(self, points: list[list[int]]) -> bool:
        [x1,y1],[x2,y2],[x3,y3]=points
        points.sort()
        if (y2-y1)*(x3-x2)!=(x2-x1)*(y3-y2):
            return True
        return False