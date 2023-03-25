def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        s1=""
        for i in word1:
            s1+=i
        s2=""
        for j in word2:
            s2+=j
        return s1==s2