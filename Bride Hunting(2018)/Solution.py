t=int(input())
for x in range(t):
    n,m=map(int,input().split())
    a=[]
    for y in range(n):
        p=list(map(int,input().split()))
        a.append(p)
    a[0][0]=0
    q=-1
    fd=10000
    u=[]
    for i in range(n):
        for j in range(m):
            s=0
            if a[i][j]==1:
                if i-1>=0:
                    if j-1>=0:
                        if a[i-1][j-1]==1:
                            s=s+1
                    if a[i-1][j]==1:
                        s=s+1
                    if j+1<m:
                        if a[i-1][j+1]==1:
                            s=s+1
                if j-1>=0:
                    if a[i][j-1]==1:
                        s=s+1
                if j+1<m:
                    if a[i][j+1]==1:
                        s=s+1
                if i+1<n:
                    if j-1>=0:
                        if a[i+1][j-1]==1:
                            s=s+1
                    if a[i+1][j]==1:
                        s=s+1
                    if j+1<m:
                        if a[i+1][j+1]==1:
                            s=s+1
            d=((i*i)+(j*j))**0.5
            if s>q:
                q=s
                fd=d
                u=[]
                u.append(i)
                u.append(j)
            if s==q and d<fd:
                u=[]
                u.append(i)
                u.append(j)
                fd=d
    print(u[0]+1,u[1]+1,q,sep=":")
