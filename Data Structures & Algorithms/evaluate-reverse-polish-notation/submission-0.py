class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token in '+-/*':
                x = st.pop()
                y = st.pop()
                if token == '+':
                    y = y+x
                elif token == '-':
                    y = y-x
                elif token =='*':
                    y = y*x
                elif token == '/':
                    y = int(y/x)
                st.append(y)
            else:
                st.append(int(token))
        return st[-1] 