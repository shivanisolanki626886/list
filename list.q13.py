n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
i=0
d=[]
while i<len(n):
    j=0
    c=0
    while j<len(n):
        if n[i]==n[j]:
            c=c+1
        j=j+1
    if n[i] not in d:
        d.append(n[i])
        print(n[i],c)
    i=i+1