
# coding: utf-8

# In[1]:


#choclete box


a=int(input())
while(a!=0):
    c=0
    n=int(input())
    l=list(map(int,input().split()))
    ma=max(l)
    e=0
    z=len(l)//2
    while(e!=z):
        cntr=0
        check=len(l)-2
        nu=1
        for i in range(len(l)-1,check,-1):
            if(l[i]!=ma):
                cntr=cntr+1
        for j in range(0,(len(l)//2)-(nu)):
            if(l[j]!=ma):
                cntr=cntr+1
        if(cntr==len(l)//2):
            c=c+1
        check=check-1
        nu=nu+1
        e=e+1
    a=a-1
    print(c) 
    
       
        


# In[ ]:


#find your gift
# cook your dish here
try:
    for _ in range(int(input())):
        n=int(input())
        s=input()
        x,y=0,0
        ll=s[0]
        if(ll=="L"):
            x-=1
        elif(ll=="R"):
            x+=1
        elif(ll=="U"):
            y+=1
        elif(ll=="D"):
            y-=1
        for i in range(1,n):
            m=s[i]
            k=s[i-1]
            if(m=="L" and k!="L" and k!="R"):
                x-=1
            elif(m=="R" and k!="L" and k!="R"):
                x+=1
            elif(m=="U" and k!="U" and k!="D"):
                y+=1
            elif(m=="D" and k!="U" and k!="D"):
                y-=1
        print(x,y)
except:
    pass


# In[ ]:


#maximize letter beauty

try:      
    def max_crossing_subarray(A,low,mid,high):
        left_sum =-1000
        sum = 0
        left_max=mid
        for i in range(mid,low-1,-1):
            sum = sum + A[i]
            if(sum>left_sum):
                left_sum = sum
                left_max = i

        right_sum = -1000
        sum = 0
        right_max = mid
        for i in range(mid+1,high+1):
            sum = sum + A[i]
            if (sum>right_sum):
                right_sum = sum
                right_max = i

        return (left_max,right_max, left_sum + right_sum)
    def max_subarray(A,low,high):
        if(high==low):
            return(low,high,A[low])
        else:
            mid=(low+high)//2

            #Getting the subarray with max sum from left, right and including mid
            llow,lhigh,lsum = max_subarray(A,low,mid)  
            rlow,rhigh,rsum = max_subarray(A,mid+1,high)
            clow,chigh,csum = max_crossing_subarray(A,low,mid,high)

            if(lsum>=rsum and lsum>=csum):
                return(llow,lhigh,lsum)
            elif(rsum>=lsum and rsum>=csum):
                return(rlow,rhigh,rsum)
            else:
                return(clow,chigh,csum)
    def alone(lis,x,y):
        maxileft=lis[x-1]
        lefind=x-1
        sul=0
        for i in range(x-1,-1,-1):
            sul+=lis[i]
            if(sul>maxileft):
                maxileft=sul
                lefind=i
        maxiright=lis[y-1]
        rigind=y-1
        sur=0
        for i in range(y-1,len(lis),1):
            sur+=lis[i]
            if(sur>maxiright):
                maxiright=sur
                rigind=i
        return (lefind,rigind,maxileft+maxiright)
    for _ in range(int(input())):
        n,q=map(int,input().split())
        b=list(map(int,input().split()))
        flag=False
        ll,rr,su=max_subarray(b,0,len(b))
        for i in range(q):
            st,x,y=input().split()
            x=int(x)
            y=int(y)
            if(st=="U"):
                b[x-1]=y
                flag=True
            elif(st=="Q"):
                if(flag==True):
                    ll,rr,su=max_subarray(b,0,len(b))
                    if(x-1>=ll and y-1<=rr):
                        print(su)
                    else:
                        lin,rin,summ=alone(b,x,y)
                        mis=0
                        if(y>x):
                            for jj in range(x,y-1):
                                mis+=b[jj]
                        elif(y==x):
                            summ-=b[x-1]
                        flag=False
                        print(mis+summ)
                        
                else:
                
                    if(x-1>=ll and y-1<=rr):
                        print(su)
                    else:
                        lin,rin,summ=alone(b,x,y)
                        mis=0
                        if(y>x):
                            for jj in range(x,y-1):
                                mis+=b[jj]
                        elif(y==x):
                            summ-=b[x-1]
                        flag=False
                        print(mis+summ)
except:
    pass

