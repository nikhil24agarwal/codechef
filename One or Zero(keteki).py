 cook your dish here
t = [int(n) for n in str(input()).split()]
x = t[0]
y = t[1]

c = []

for i in range(0,x):
    c.append(str(input()))

a = 0
b= 0

for i in range(0,x):
    for j in range(0,len(c[i])):
      
        if c[i][j] == '#':
            start = j
            k = j+1
            while c[i][k] == '#':
                k = k+1
            k = k-1

            if k - j > 1:
                a1 = 0
                for l in range(i+1,x):
                    if c[l][start] == '#' and c[l][k] == '#':
                        b = 1
                        for m in range(start+1,k):
                            if c[l][m] == '.':
                                a1 = a1 + 1
                                a = a + 1
                        
                    if a1 == 0:
                        break
        
if a>0 and b>0:
    print("0")

else:
    print("1")
