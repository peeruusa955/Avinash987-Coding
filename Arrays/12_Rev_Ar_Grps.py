"""
Given an array arr[] of positive integers of size N.
Reverse every sub-array of K group elements.
"""
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    if k>n:
        k=n
    l=list(map(int,input().split()))
    cnt=0
    while(cnt<n):
        if(cnt<cnt+k):
            tmp=l[cnt:cnt+k]
            cnt=cnt+k
            tmp.reverse()
            for k in tmp:
                print(k,end=' ')
        else:
            tmp=l[cnt:n]
            cnt=cnt+len(tmp)
            tmp.reverse()
            for k in tmp:
                print(k,end=' ')
    print()