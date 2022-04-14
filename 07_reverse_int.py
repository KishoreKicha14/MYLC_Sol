class Solution:
    def reverse(self, x: int) -> int:
        neg=0
        if x<0:
            neg=1
            x=x*-1
        s=0
        while(1):
            r=0
            r=x%10
            x=x//10
            s=s*10+r
            if s < (-2**31) or s >((2**31)-1):#the range of the Int32 is -2**32 to 2**32-1.
                return 0
            if x==0:
                if neg==1:
                    return s*-(1)
                else:
                    return s
