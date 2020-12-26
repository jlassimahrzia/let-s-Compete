
L = []

ch=str(input("donner chaine : "))
k=0

for i in range(len(ch)):
    h=i+ord(ch[i])-65
    if h>k:
        k=h
k+=1
for i in range(k):
    L.append(' ')
for i in range(len(ch)):
    u=i+ord(ch[i])-65
    L[u]=ch[i]

str1 = ''.join([str(elem) for elem in L]) 
print(str1)
