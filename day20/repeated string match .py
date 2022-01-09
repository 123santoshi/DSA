def repeatedStringMatch(self, A, B):
        # code here
        ans=1
        a1=A
        while(len(A)<len(B)):
            ans+=1
            A+=a1
        if B in A:
            return ans
        if B in A+a1:
            return ans+1
        return -1
