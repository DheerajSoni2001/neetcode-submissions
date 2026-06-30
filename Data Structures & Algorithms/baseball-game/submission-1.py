class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        st = []

        for x in operations:
            if x == "+" and len(st)>=2:
                a = st.pop()
                b = st.pop()
                c = a+b
                st.append(b)
                st.append(a)
                st.append(c)
            elif x == "C" and len(st) >= 1:
                st.pop()
            elif x == "D" and len(st) >= 1:
                a = st.pop()
                b = a*2
                st.append(a)
                st.append(b)
            else:
                st.append(int(x))
        return sum(st)