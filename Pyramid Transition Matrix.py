class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        from collections import defaultdict

        mp = defaultdict(list)
        for a in allowed:
            mp[a[0] + a[1]].append(a[2])

        memo = {}

        def dfs(row):
            if len(row) == 1:
                return True
            if row in memo:
                return memo[row]

            def build(i, next_row):
                if i == len(row) - 1:
                    return dfs(next_row)
                key = row[i] + row[i + 1]
                if key not in mp:
                    return False
                for c in mp[key]:
                    if build(i + 1, next_row + c):
                        return True
                return False

            memo[row] = build(0, "")
            return memo[row]

        return dfs(bottom)
