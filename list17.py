print('Aapka Sawaal hai')
print('What is the capital of india?')
a=['chandigarh','Bhopal','Chennai','Delhi']
i=0
while i<len(a):
     print(i+1,a[i])
     i=i+1
n=int(input('select your answer'))
j=0
c=4
b=[1,2,3,4]
while j<len(b):
     if n==c:
         print('Congrats! Aapka answer sahi hai')
         break
     if n not in b:
         print('Exit')
         break
     else:
         print('Sadly salla javab galathai')
         break
     j=j+1