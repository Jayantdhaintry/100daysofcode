def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""

        output = strs[0]
        for i in range(len(output)):
            for word in strs[1:]:
                if (i == len(word) or word[i] != output[i]):
                    return output[0:i]

        return output
