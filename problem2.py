def digPow(n,p):
  s=0
  L=list(str(n))
  for i in range(0,len(L)):
    s+=int(L[i])**p
    p+=1
  p=s/n;
  if (s%n==0):
    return int(p)
  else :
    return -1
