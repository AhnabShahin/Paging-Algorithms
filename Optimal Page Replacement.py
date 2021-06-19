a = []
sum = 0
f = int(input('Input Memory Size : '))

input_Pages = (input('Input queue : ')).strip(' ')
a = input_Pages.split(' ')
print("Inputs are: ", a)

n=len(a)
m=[]
c=[]
l=[]
for i in range(f):
    m.append(-1)

print('\nOutput wil be: ')
for i in range(n):
    test=0
    for p in range(f):
        c.append(m[p])
    if i<f:
        m[i]=a[i]
        sum+=1
        a[i]=-99
    else:
        for j in range(f):
            if a[i]==m[j]:
                test=1
                a[i]=-99
                break
        if test==0:
            for s in range(f):
                if(m[s] in a):
                    l.append(a.index(m[s]))
                else:
                    l.append(999)
            idx=l.index(max(l))
            m[idx]=a[i]
            sum+=1
            a[i]=-99


    if c==m:
        for q in range(f):
            print('-',end=' ')
    else:
        for q in range(f):
            if m[q]==-1:
                print("-",end=' ')
            else:
                print(m[q],end=' ')
    c.clear()
    l.clear()
    print()

print("Page Fault: ",sum)