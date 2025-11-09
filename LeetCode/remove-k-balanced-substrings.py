class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        st = s
        rem = "(" * k + ")" * k
        while rem in st:
            st = st.replace(rem, "")
        return st