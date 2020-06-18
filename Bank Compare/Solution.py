k=int(input())
for i in range(k):
    p=float(input())
    t=(input())
    a=[]
    for j in range(2):
        n=int(input())
        s=0
        for x in range(n):
            y,r=map(float,input().split())
            num=p*r
            den=1-(1/((1+r)**(12*y)))
            emi=num/den
            s=s+emi
        a.append(s)
    if a[0]<a[1]:
        print("Bank A")
    else:
        print("Bank B")
    
