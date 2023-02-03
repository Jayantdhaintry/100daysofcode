def mostWordsFound(self, sentences: list[str]) -> int:
        count=0
        for i in sentences:
            c=len(i.split())
            if c>count:
                count=c
        return count