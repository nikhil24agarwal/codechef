
# coding: utf-8

# In[ ]:


#Chef Swaps Digits
T = int(input())

for i in range(T):
    A,B = input().split()
    summax = int(A)+int(B)
    A,B = list(A),list(B)
    
    for a in range(len(A)):
        for b in range(len(B)):
            temp = A[a]
            A[a] = B[b]
            B[b] = temp
            check = int("".join(A)) + int("".join(B))
            if(check>summax):
                summax = check
            temp = A[a]
            A[a] = B[b]
            B[b] = temp
    
    print(summax)
    


# In[ ]:


T=int(input())
z=0
while(z<T):
    S=input()
    a=list(map(int,input().strip().split()))[:2]
    K,X=a
    ans=0
    D={}
    for i in range(len(S)): 
        if(S[i]in D):
            D[S[i]]+=1
        else: 
            D[S[i]]=1

        if(D[S[i]]<=X and K>=0):
            ans+=1
        else:
            K-=1
            continue
    #print(D)
    print(ans)    
    z+=1

