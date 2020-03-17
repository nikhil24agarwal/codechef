
# coding: utf-8

# In[ ]:


#include <iostream>
#C plus plus 

using namespace std;

int main()
{
    int t;
    cin >> t;
    for (int j=0; j<t; j++){
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }
        for(int i = 1;i < n; ++i)
    {
       if(a[0] < a[i]){
           a[0] = a[i];}
    }
    cout << a[0]<<endl;
    }

    return 0;
}


# In[ ]:


# cook your dish here
try:
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=input().split()
        su=[]
        a[0]=int(a[0])
        a[1]=int(a[1])
        a[2]=int(a[2])
        s=a[0]+a[1]+a[2]
        if(n==3):
            print(s)
        else:
            su.append(s)
            maxi=s
            for i in range(3,n):
                a[i]=int(a[i])
                m=a[i-2]+a[i-1]+a[i]
                su.append(m)
                if(m>maxi):
                    maxi=m
            p=a[-1]+a[-2]+a[0]
            q=a[-1]+a[0]+a[1]
            if(p>maxi):
                maxi=p
            if(q>maxi):
                maxi=q
            print(maxi)
except:
    pass

