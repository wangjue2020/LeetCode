class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        for i in range(len(tokens)):
            if tokens[i].isdigit() or len(tokens[i]) > 1:
                l.append(tokens[i])
            else:
                operator = tokens[i]
                second = int(l.pop())
                first = int(l.pop())
                if operator == '+':
                    l.append(second+first)
                elif operator == '-':
                    l.append(first - second)
                elif operator == '*':
                    l.append(first * second)
                else:
                    l.append(first/second)
        return int(l[0])