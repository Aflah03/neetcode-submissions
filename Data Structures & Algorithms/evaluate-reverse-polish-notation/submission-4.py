class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for item in tokens:
            if item in '+-/*':
                print("item is ", item)
                y = st.pop()
                x = st.pop()
                if item == '+':
                    x = x+y
                elif item == '-':
                    x = x-y
                elif item == '*':
                    x = x*y
                else:
                    x= (int(x/y))
                st.append(x)
            else:
                st.append(int(item))
        return st[-1]