class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generate(cur=[]):
            if len(cur) == 2*n:
                cur_str = ''.join(cur)
                if valid(cur_str):
                    ans.append(cur_str)
            else:
                generate(cur[:]+['('])
                generate(cur[:]+[')'])
        def valid(cur_str):
            balance = 0
            for char in cur_str:
                if char == '(':
                    balance+=1
                else:
                    balance-=1
                if balance < 0:
                    return False
            return balance == 0
        generate()
        return ans