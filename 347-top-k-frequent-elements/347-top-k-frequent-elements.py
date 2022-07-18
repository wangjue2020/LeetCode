class Solution:
    def topKFrequent(self, nums, k) :
        nums.sort()
        l = []
        cur = nums[0]
        cur_freq = 1
        for i in range(1, len(nums)):
            if cur == nums[i]:
                cur_freq += 1
            else:
                if l == []:
                    l.append((cur, cur_freq))
                else:
                    l = self.addto(l, cur, cur_freq,k)
                cur = nums[i]
                cur_freq = 1
        l = self.addto(l,cur, cur_freq,k)
        l = [i[0] for i in l]
        return l[:k]
    def addto(self, l, cur, cur_freq,k):
        f = False
        for i in range(len(l)):
            if l[i][1] < cur_freq:
                l = l[:i]+[(cur, cur_freq)]+l[i:]
                f = True
                break
        if not f:
            l.append((cur, cur_freq))
        if len(l) > k:
            l = l[:-1]
        return l