class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for chr in columnTitle:
            x=ord(chr)-ord('A')+1
            res = res*26+x

        return res
