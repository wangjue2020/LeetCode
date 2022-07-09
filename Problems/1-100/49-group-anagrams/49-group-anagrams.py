class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            cur = strs[i]
            sorted_cur = "".join(sorted(cur))
            if sorted_cur in d:
                d[sorted_cur].append(cur)
            else:
                d[sorted_cur] = [cur]
        return d.values()