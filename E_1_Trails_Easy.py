from functools import lru_cache
import sys
sys.setrecursionlimit(10000)  # Increased recursion limit

MOD = 10**9 + 7

@lru_cache(maxsize=None)
def recur(pos,move,day):
    if pos!=-1 and day==n:
        return 1
    ans=0

    if pos!=-1:  # At cabin
        if s[pos]!=0:
            ans=ans+s[pos]*(recur(-1,"s",day+1))
        if l[pos]!=0:
            ans=ans+l[pos]*(recur(-1,"l",day+1))
    else:  # At lake
        if move=="s":  # After short path
            for k in range(m):  # Check all cabins
                if s[k]!=0:  # If cabin has short path
                    ans=(ans+s[k]*recur(k,"s",day))
                if l[k]!=0:  # If cabin has long path
                    ans=(ans+l[k]*recur(k,"l",day))
        else:  # After long path
            for k in range(m):  # Check all cabins
                if s[k]!=0:  # Can only use short paths
                    ans=(ans+s[k]*recur(k,"s",day))
    return ans%MOD

# Input reading
m,n=map(int,input().split())
s=list(map(int,input().split()))
l=list(map(int,input().split()))

print(recur(0,"None",0))