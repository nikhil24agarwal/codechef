
# coding: utf-8

# In[ ]:


#pintu and fruits
#c++
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        vector<int>v(n),p(n);
        for(int i=0;i<n;i++)
        cin>>v[i];
        for(int i=0;i<n;i++)
        cin>>p[i];
        map<int,int>m;
        for(int i=0;i<n;i++)
        m[v[i]]+=p[i];
        int mx=INT_MAX;
        for(auto itr:m)
            if(itr.second<mx)
            mx=itr.second;

        cout<<mx<<"\n";
    }
}


# In[ ]:


#XOR EMGine
#include<bits/stdc++.h>
using namespace std;
int se(int a)
{
    int count=0;
   while(a)
   {
       count++;
       a=a & (a-1);
   }
   return count;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while(t--)
    {
        int n,q;
        cin>>n>>q;
        vector<int>v(n);
        int count=0;
        for(int i=0;i<n;i++)
        {
        cin>>v[i];
        if(se(v[i])%2==0)
        count++;
        }
        while(q--)
        {
         int p;
         cin>>p;
         int r=se(p);
         if(r%2==0)
         cout<<count<<" "<<n-count<<"\n";
         else
         cout<<n-count<<" "<<count<<"\n";
        }

    }
}


# In[ ]:


#ada bishop2
#C++
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int x,y;
        cin>>x>>y;
        vector<pair<int,int> >v;
        v.push_back({x,y});
        int r,c;
        int p=(x-y)/2;
         r=x-p;
         c=y+p;
        int a=r,b=c,i=r-1;
        while(a>1 && b>1)
        {
            v.push_back({a,b});
            if(a<=4 && b<=4)
            {v.push_back({2*a-1,1});
            v.push_back({1,2*b-1});
            }
            else
            {
              v.push_back({8,2*a-8});
              v.push_back({2*a-8,8});

            }
            v.push_back({a,b});
            a--;
            b--;
        }
        v.push_back({a,b});
        while(a<=r && b<=c)
        {
            v.push_back({a,b});
            a++;
            b++;
        }
        while(a<8 && b<8)
        {
            v.push_back({a,b});
             if(a<=4 && b<=4)
            {v.push_back({2*a-1,1});
            v.push_back({1,2*b-1});
            }
            else
            {
              v.push_back({8,2*a-8});
              v.push_back({2*a-8,8});

            }
            v.push_back({a,b});
            a++;
            b++;
            v.push_back({a,b});
        }
        vector<pair<int,int> >e;
        if(a==8 && b==8 && r!=8 && c!=8)
        v.push_back({8,8});
        e.push_back(v[0]);
        for(int i=1;i<v.size();i++)
        if(v[i]!=e[e.size()-1])
        e.push_back(v[i]);
        cout<<e.size()<<"\n";
        for(int i=0;i<e.size();i++)
        cout<<e[i].first<<" "<<e[i].second<<"\n";

    }
}


# In[ ]:


#lasers
#python
#partially correct


T = int(input())

for i in range(T):
    N,Q = map(int,input().split())
    Ypoints = list(map(int,input().split()))
    for i in range(Q):
        X1,X2,Y = map(int,input().split())
        count = 0
        for c in range(X1-1,X2-1,1):
            if((Ypoints[c]<Y+1 and Ypoints[c+1]>Y-1) or (Ypoints[c]>Y-1 and Ypoints[c+1]<Y+1)):
                count+=1
        print(count)


# In[ ]:


#break
#partially correct
try:
    t,s=list(map(int,input().split()))
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a.sort()
        b.sort()
        if(b[0]<=a[0]):
            print("NO")
        else:
            c=set([a[0],b[0]])
            flag=True
            for j in range(1,n):
                if(b[j]<=a[j] or a[j] not in c):
                    flag=False
                    break
                else:
                    c=c|set([a[j],b[j]])
            if(flag):
                print("YES")
            else:
                print("NO")
except:
    pass

