class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for token in tokens:
            if token not in ['+', '-', '/', '*']:
                stack.append(token)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                res = eval(f'{num2}{token}{num1}')
                stack.append(int(res))
        return stack[0]
                