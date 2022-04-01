element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even_sum=0
odd_sum=0
c=0
while i<len(element):
    if element[i]%2==0:
        even_sum=even_sum+element[i]
    else:
        odd_sum=odd_sum+element[i]
        c=c+1
    i=i+1
print(even_sum,even_sum/10,c)
print(odd_sum,odd_sum/10,c)
