# number=[50,40,23,70,56,12,5,10,7]
# i=0
# max1=0
# while i<len(number):
#     if number[i]>max1:
#         max1=number[i]
#     i=i+1

number=[50,40,23,70,56,12,5,10,7]
i=0 
max=0
while i<len(number):
    if number[i]>max:
        max=number[i]
    i=i+2
print(max)



