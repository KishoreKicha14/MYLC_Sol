class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d={}
        l=len(s)
        if numRows<2:
            return s
        n=numRows*2-2
        for i in range(l):
                if i%n<numRows:
                    if i%n not in d:
                        d[i%n]=s[i]
                    else:
                        d[i%n]=d[i%n]+s[i]
                elif i%n>=numRows:
                    d[n-i%n]=d[n-i%n]+s[i]
        p=""
        for i in d:
            p=p+d[i]
        return p
