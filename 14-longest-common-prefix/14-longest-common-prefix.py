class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        tmp = strs[0]
        rest = strs[1:]
        res = ""
        i = 0
        while (i < len(tmp)):
            found = True
            for s in rest:
                if i >= len(s) or tmp[i] != s[i]:
                    found = False


            if not found:
                break
            else:
                res += tmp[i]
                i = i + 1
        return res