class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for char in s:
            if char== '(' or char== '{' or char == '[':
                st.append(char)
            
            else:
                if not st:
                    return False
                top_item = st[-1]
                if (char == ']' and top_item=='[') or (char=='}' and top_item=='{') or (char==')' and top_item=='('):
                    st.pop()
                else:
                    return False
        return len(st) == 0