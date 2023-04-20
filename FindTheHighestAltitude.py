def largestAltitude(self, gain: list[int]) -> int:
        output = 0
        present_Height = 0

        for h in gain:
            present_Height += h
            
            output = max(output, present_Height)
        
        return output