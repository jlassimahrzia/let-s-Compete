
def space(ch):
    t=[]
    i=65
    for c in ch:
       t+=[' ']*26
       t[ord(c)-i]=c
       i=i-1
    return ''.join(t)
