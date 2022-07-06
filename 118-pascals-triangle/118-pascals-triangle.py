class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            cur = []
            if i == 0:
                cur = [1]
                ans.append(cur)
            elif i == 1:
                cur = [1,1]
                ans.append(cur)
            else:
                last = ans[-1]
                for i in range(len(last)-1):
                    cur.append(last[i]+last[i+1])
                cur = [1]+cur+[1]
                ans.append(cur)
        return ans