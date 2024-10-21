class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for char in expression:
            if char == ')':
                sub_expr = []
                while stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()

                operator = stack.pop()

                if operator == '!':
                    stack.append('t' if sub_expr[0] == 'f' else 'f')
                elif operator == '&':
                    stack.append('t' if all(x == 't' for x in sub_expr) else 'f')
                elif operator == '|':
                    stack.append('t' if any(x == 't' for x in sub_expr) else 'f')
            
            elif char != ',':
                stack.append(char)
        
        return stack[0] == 't'