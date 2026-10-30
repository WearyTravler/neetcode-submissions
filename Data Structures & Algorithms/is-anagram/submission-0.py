class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        s_sorted = "".join(sorted(s_list))
        t_sorted = "".join(sorted(t_list))
        if sorted(s_sorted) == sorted(t_sorted):
            return True
        else:
            return False


        