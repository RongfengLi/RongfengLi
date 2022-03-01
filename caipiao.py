import random
def all_number_str():
    a=random.sample(range(1,34),6)
    b=random.sample(range(1,12),2)
    if b[0]<10:
        b='0'+str(b[0])
    else:
        b=str(b[0])
    strs=''
    for i in a:
        if i<10:
            strs+='0'+str(i)+' '
        else:
            strs+=str(i)+' '
    return strs+b
print(all_number_str())
