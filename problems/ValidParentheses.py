class ValidParentheses(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        cor = True
        for i in s:
            if i == '(':
                stack.append('(')
            elif i == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    cor = False
                    break
                elif stack[-1] == '(':
                    stack.pop()
            if i == '[':
                stack.append('[')
            elif i == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    cor = False
                    break
                elif stack[-1] == '[':
                    stack.pop()
            if i == '{':
                stack.append('{')
            elif i == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    cor = False
                    break
                elif stack[-1] == '{':
                    stack.pop()
        if (cor and len(stack) == 0):
            return True
        else:
            return False


if __name__ == '__main__':
    sol = ValidParentheses()
    print(sol.isValid("({[(]})"), "expected False")
    print(sol.isValid("({[()]})"), "expected True")