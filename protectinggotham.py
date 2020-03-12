test_str=str(input())
test_str1=str(input())

l=list(map(int,input().split()))


all_freq = {} 
  
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
        
print(all_freq)


all_freq1 = {} 
  
for i in test_str1: 
    if i in all_freq1: 
        all_freq1[i] += 1
    else: 
        all_freq1[i] = 1
        
print(all_freq1)

c=0
for z in l:
    a=test_str[z-1]
    for a in all_freq:
        if(a in all_freq1):
            if(all_freq[a]>all_freq1[a]):
                all_freq[a]=all_freq[a]-1
                c=c+1
            else:
                break
            
        else:
            c=c+1
print(c) 
