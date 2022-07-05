class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0':
            return 0
        l = [1]
        for i in range(len(s)):
            if i == 0:
                l.append(1)
                continue
            cur = 0
            if s[i] != '0':
                cur += l[-1]
            if int(s[i-1:i+1]) > 0 and int(s[i-1:i+1]) <= 26 and s[i-1] !='0':
                cur += l[-2]
            if cur == 0:
                return 0
            else:
                l.append(cur)
        return l[-1]