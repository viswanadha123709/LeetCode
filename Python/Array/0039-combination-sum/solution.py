class Solution(object):
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(idx, curr, terms):

            if curr == target:
                result.append(terms[:])
                return

            if curr > target or idx == len(candidates):
                return

            terms.append(candidates[idx])
            backtrack(idx, curr + candidates[idx], terms)

            terms.pop()

            backtrack(idx + 1, curr, terms)

        backtrack(0, 0, [])
        return result