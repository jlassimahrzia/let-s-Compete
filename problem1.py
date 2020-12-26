n=int(input("donner n: "))
ch=str(n)
somme=0
p=int(input("donner p: "))
for i in range(len(ch)):
    somme+=int(ch[i])**(p)
    p+=1
if somme % n ==0:
    print(somme//n)
else:
    print("-1")
