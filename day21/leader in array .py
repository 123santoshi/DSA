 def leaders(self, a,n):
        #Code here
        l=[]
        m=a[n-1]
        for i in range(n-1,-1,-1):
            if(a[i]>=m):
                l.append(a[i])
                m=a[i]
        l=reversed(l)
        return l
