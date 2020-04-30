def rev(n):
    r=0
    while(n>0):
        rem=n%10
        r=r*10+rem
        n=int(n/10)
    return r