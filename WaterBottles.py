def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        if numBottles<numExchange:
            return numBottles
        else:
            total=numBottles
            empty=numBottles
            while(empty>=numExchange):
                total=total+(empty//numExchange)
                empty=(empty%numExchange)+(empty//numExchange)
            return total