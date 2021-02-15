#ip address
'''import ipaddress
def ip_address(add):
    try:
        x=int(add)
        z=ipaddress.ip_address(add)
    except:
        addr1 = ipaddress.ip_address(add)  
        return(int(addr1))'''

#hex
'''def hex(num):
    print(num)
    if 'num' in num[0]:
        print(num[0][:4])
        print(int(num[0][:4],16),int(num[0][4:6],16),int(num[0][6:],16))
    else:
        a,b,c=x
        print(hex(int(a))+hex(int(b)).replace("x","")+hex(int(c)).replace("0x",""))'''




#isogram
'''def check_isogram(str1):
 print(True if len(list(str1))==len(set(str1)) else False)'''




#mexican wave
'''def mexican_wave(x):
    temp=[print("".join(x[:i])+"".join(x[i].upper())+"".join(x[i+1:])) for i in range(len(x))]'''

'

#shuffle no
'''def shuffle(a):
    dict1={}
    for i in a:
        if i not in dict1.keys():
            dict1[i]=a.count(i)
        else:
            continue
    print(dict1)'''


#permutation
'''from itertools import permutations
def permutation(num):
    x=permutations(num)
    list1=[]
    for i in x:
        list1.append(int("".join(i)))
        print(max(list1))'''


