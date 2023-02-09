def maximumWealth(self, accounts: list[list[int]]) -> int:
        c = sum(accounts[0])
        for i in accounts:
            c = max(c, sum(i))
        return c