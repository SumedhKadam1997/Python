d={}
conti=set()
with open ('country.txt','r+') as f:
    for i in f:
        i = i.rstrip()
        j = i.split(',')
        conti.add(j[4])
    print(conti)
    
    for k in conti:
        d[k]=[]
        f.seek(0)
        for i in f:
            i = i.rstrip()
            j = i.split(',')
            if k in j:
                d[k].append(j[0])
f.close()
 
for i in range(65,91):
    print(chr(i))
    count=0
    for l,j in d.items():
        for k in j:
            
            if chr(i) == k[0]:
                count+=1
                print('  '+l)
                print('            '+k)
    print('            '+'------------')            
    print('             '+str(count))