def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        output = 0
        n=len(points)
        for i in range(n-1):
            dx = abs(points[i+1][0] - points[i][0])
            dy = abs(points[i+1][1] - points[i][1])
            
            output = output + max(dx,dy)
        
        return output