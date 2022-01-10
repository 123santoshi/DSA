def findNth(self,n):
        #code here
        pos=1
        r=0
        while(n>0):
            r=r+(n%9)*pos
            n=n//9
            pos*=10
        return r
