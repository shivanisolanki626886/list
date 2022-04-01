kitna_paisa_hai=[3000,600000,324990909,90990900,30000,510,4100]
i=0
c1=0
c2=0
c3=0
while i<len(kitna_paisa_hai):    
    if kitna_paisa_hai[i]>100000000:
        c1=c1+1
    elif kitna_paisa_hai[i]>10000000:
        c2=c2+1
    else:
        c3=c3+1
    i=i+1
print("crorepati",c1)
print("lakhpati",c2)
print("dilwale",c3)

