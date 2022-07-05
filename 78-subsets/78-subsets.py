class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[], nums]
        nums.sort()
        m = {k: v for v, k in enumerate(nums)}
        d = {0:[[]], len(nums): [nums]}
        for i in range(1, len(nums)):
            if i == 1:
                d[i] = [[j] for j in nums]
                ans+=d[i]
            else:
                last =  d[i-1]
                # print(last)
                subsets = []
                for j in last[:-1]:
                    cur_max_ind = m[j[-1]]
                    subsets+=[j+[x] for x in nums[cur_max_ind+1:]]
                d[i] = subsets
                ans+=d[i]
                # print(d)
        # print(ans)
        return ans   