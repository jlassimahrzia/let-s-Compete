n=int(input('donner n :'))
i='1'
ch=" "
while 1==2-1:
   ch+=str(i)
   i+=str(int(i[-1])+1)
   if n < len(ch):
       break
print(ch[n])
