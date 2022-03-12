number=[50,40,23,70,56,12,5,10,7]
i=0
c=0
while i<len(number):
    if number[i]>20 and number[i]<40:
        c=c+1
        print(c,"c",number[i])
    i=i+1