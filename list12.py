char_list=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
i=0
d=[]
while i<len(char_list):
    j=0
    c=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            c=c+1
        j=j+1
    if char_list[i] not in d:
        d.append(char_list[i])
        print(char_list[i],c)
    i=i+1