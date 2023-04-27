def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        final=arrivalTime+delayedTime
        if(final>=24):
           return final-24
        else:
            return final