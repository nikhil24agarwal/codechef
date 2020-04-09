
# coding: utf-8

# In[ ]:


#walter and cheese


try:
    for _ in range(int(input())):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        x=max(a)
        y=max(b)
        if(x!=y):
            print("YES")
        else:
            print("NO")
    
    
    
except:
    pass


# In[ ]:


#another game of numbers

try:
    for _ in range(int(input())):
        a,b=map(int,input().split())
        y=list(bin(b).replace("0b",""))
        x=list(bin(a).replace("0b",""))
        if(b>a):
            k=len(y)-len(x)
            for _ in range(k):
                x.insert(0,"0")
        else:
            k=len(x)-len(y)
            for _ in range(k):
                y.insert(0,"0")
        xor=a^b
        shi=0
        ind=0
        for _ in range(len(y)-1):
            k=y.pop(-1)
            y.insert(0,k)
            ind+=1
            lll=(int("".join(x),2))^(int("".join(y),2))
            if(lll>xor):
                xor=lll
                shi=ind
        print(shi,xor)
            
        
                
    
except:
    pass


# In[ ]:


#partial (A lot pf cars)

try:
# if(True):
    for _ in range(int(input())):
        m,n=map(int,input().split())
        c=[]
        coun=0
        for i in range(m):
            k=list(input().split())
            co=0
            k.append(-1)
            k.append(-1)
            for j in range(n):
                if(k[j]=="P"):
                    co+=1
                    if(co==1):
                        k[-2]=j
                    k[-1]=j
            c.append(k)
        if(m==2):
            if(c[1][-1]==-1):
                coun=c[0][-1]-c[0][-2]
            elif(c[0][-1]==-1):
                coun=c[1][-1]-c[1][-2]
            else:
                coun=c[0][-1]-c[0][-2]
                if(c[1][-1]>c[0][-1]):
                    coun+=c[1][-1]-c[0][-1]
                else:
                    coun+=c[0][-1]-c[1][-1]
                coun+=c[1][-1]-c[1][-2]+1
            print(coun)
        else:
            coun=c[0][-1]-c[0][-2]
            print(coun)
            
except:
    pass
        


# In[ ]:


# a lot of car another try
try:
    test=int(input())
    while(test!=0):


        l=list(map(int,input().split()))
        m=l[0]
        lenn=l[1]
        n=l[1]
        arrayl=[]
        arrayr=[]
        
        while(m!=0):
            check=list(map(str,input().split()))
            c=0
            
            for i in range(0,n):
                c=c+1
                if(check[i]=='P'):
                    arrayl.append(i+1)
                    break
                if(c==lenn):
                    arrayl.append(-1)
                    arrayr.append(-1)
                    c=0
                 
                                
                                                

                    
                    
                    
            for j in range(n-1,-1,-1):
                if(check[j]=='P'):
    
                    arrayr.append(j+1)
                    break
            m=m-1
            
    
    
        m=lenn          
        sum=0
        for z in range(0,m):    #m krna h yha
            a=max(arrayr[z],arrayl[z])
            b=min(arrayr[z],arrayl[z])
            sum=sum + (a-b)
    
    
    
        #sum=sum+(m-(floor+1))
        #m krna h yha
        floor=0
        for g in range(m):
            if(arrayl[g]==-1):
                floor=g+1
                
    
    
    
    
        for q in range(0,m-1):     #m-1 krna h
            if(arrayl[q]==-1):
                continue
                
        arrayll=[]
        for i in arrayl:
            if(i!=-1):
                arrayll.append(i)
                
        arrayrr=[]
        for i in arrayr:
            if(i!=-1):
                arrayrr.append(i)
        
            
            
            
        for q in range(0,m-1):     #m-1 krna h
            if(q%2!=0):
                ma=max(arrayll[q],arrayll[q+1])
                mi=min(arrayll[q],arrayll[q+1])
                sum=sum+(ma-mi)
            if(q%2==0):
                mar=max(arrayrr[q],arrayrr[q+1])
                mir=min(arrayrr[q],arrayrr[q+1])
                sum=sum+(mar-mir)
        
        sum=sum-floor
        sum=sum+ (m -(floor+1))
        print(sum)
        test=test-1
except:
    pass


# In[ ]:


#corona in korananagar
try:
# if(True):
    for _ in range(int(input())):
        n=int(input())
        st=list(input())
        d=int(input())
        p=list(map(int,input().split()))
        c=0
        
        for i in range(d):
#             print(s11,"fi")
            st.insert(p[i]-1+i,"|")
            
            m=[]
            for j in range(len(st)):
                if(st[j]=="1"):
                    m.append(j)
            c=len(m)
            for j in m:    
                if(j!=0 and st[j-1]=="0"):
                    st[j-1]="1"
                    c+=1
                if(j!=len(st)-1 and st[j+1]=="0"):
                    st[j+1]="1"
                    c+=1
                        
        print(c)
        
except:
    pass

#a lot of car full

try:
# if(True):
    for _ in range(int(input())):
        m,n=map(int,input().split())
        c=[]
        last=0
        flag=True
        rowstart=0
        rowend=0
        for i in range(m):
            k=list(input().split())
            co=0
            k.append(-1)
            k.append(-1)
            for j in range(len(k)):
                if(k[j]=="P"):
                    co+=1
                    if(co==1):
                        k[-2]=j
                    k[-1]=j
                    rowend=i
                
            if(k[-1]!=-1 and flag):
                flag=False
                rowstart=i
                if(i%2==0):
                    last=k[-2]
                else:
                    last=k[-1]
            c.append(k)
        count=0
#         print(c)
        
        for i in range(rowstart,rowend+1):
            
            if(i%2==0 and c[i][-1]!=-1):
                count+=abs(last-c[i][-2])
                count+=c[i][-1]-c[i][-2]
                last=c[i][-1]
            elif(i%2!=0 and c[i][-1]!=-1):
                count+=abs(last-c[i][-1])
                count+=c[i][-1]-c[i][-2]
                last=c[i][-2]
            count+=1
        print(count-1)
    
    
    
except:
    pass


#CODEKARO partial

try:
# if(True):
    
    def modInverse(a,m) : 
        m0=m
        y=0
        x=1
        if(m==1): 
            return 0
        while(a>1):
            q=a//m
            t=m
            m=a%m
            a=t
            t=y
            y=x-q*y
            x=t
        if(x<0): 
            x=x+m0 
        return x 
    
    
    for _ in range(int(input())):
        m=10**9+7
        n,k=map(int,input().split())
        for _ in range(n):
            l=int(input())
            lll=l//2
            down=pow(52,lll,m)
            tot=modInverse(down,m)
            print(tot)
except:
    pass


#corona scare partial

try:
# if(True):
    for _ in range(int(input())):
        x=int(input())
        n=int(input())
        a=list(map(int,input().split()))
        m=int(input())
        b=list(map(int,input().split()))
            
        count=0
        for j in range(m-n+1):
            dif=b[j]-a[0]
            if(dif>=0 and dif<=x):
                flag=True
                ind=0
                k=j
                for _ in range(n):
                    if(b[k]-dif!=a[ind]):
                        flag=False
                        break
                    ind+=1
                    k+=1
                if(flag):
                    count+=1
            elif(dif<0 and (-1*dif)<=x):
                flag=True
                ind=0
                k=j
                for _ in range(n):
                    if(a[ind]+dif!=b[k]):
                        flag=False
                        break
                    ind+=1
                    k+=1
                if(flag):
                    count+=1
        print(count)
    
except:
    pass


#maximum product multiple (partial)


try:
# if(True):
    for _ in range(int(input())):
        a,b,k=map(int,input().split())
        li=[]
        fn=[]
        f=0
        maxsum=0
        maxx=0
        for i in range(a,b+1):
            if(i%k==0):
                f=i
                break
        if(f==0):
            print(-1)
            continue
        for i in range(f,b+1,k):
            if(i%10==0):
                continue
            else:
                ss=str(i)
                flag=False
                summ=1
                for j in range(len(ss)-1):
                                      
                    if(ss[j]=="0"):
                        flag=True
                        break
                        
                    iiflag=False
                    for p in range(j+1,len(ss)):
                        if(ss[p]=="0"):
                            break
                        
                        if(int(ss[j])%int(ss[p])==0):
                            iiflag=True
                            break
                    if(iiflag==False):
                        flag=True
                        break
                    summ*=int(ss[j])
                if(flag):
                    continue
                else:
                    summ*=int(ss[-1])
                    li.append(i)
                    fn.append(summ)
                    if(maxsum<summ):
                        maxsum=summ
                        maxx=i
        if(maxx!=0):
            print(maxsum,maxx)
        else:
            print(-1)
                    
                    
    
    
    
except:
    pass

