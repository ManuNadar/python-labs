#ip address
'''import ipaddress
def ipaddress_address(add):
    try:
        x=int(add)
        z=ipaddress.ip_address(add)
    except:
        addr1 = ipaddress.ip_address(add)  
        return(int(addr1))'''


'''def hex(num):
    print(num)
    if 'num' in num[0]:
        print(num[0][:4])
        print(int(num[0][:4],16),int(num[0][4:6],16),int(num[0][6:],16))
    else:
        a,b,c=x
        print(hex(int(a))+hex(int(b)).replace("x","")+hex(int(c)).replace("0x",""))'''


#largest no by shuffling the digits





#isogram
'''def check_isogram(str1):
 print(True if len(list(str1))==len(set(str1)) else False)'''




#mexican wave
'''def mexican_wave(x):
    temp=[print("".join(x[:i])+"".join(x[i].upper())+"".join(x[i+1:])) for i in range(len(x))]'''

'''def Deleting_singal_digit(lis_t):
    z=0
    lis_t=[]
    lis_t_2=[]
    for i in range(len(lis_t)):
        lis_t_2=lis_t.copy()
        lis_t_2.pop(z)
        lis_t.append(int("".join(lis_t_2)))
        z+=1
    print(max(lis_t))'''
def Highest_num_suffule(x):
    dic_t={}
    for i in x:
        if i not in dic_t.keys():
            dic_t[i]=x.count(i)
        else:
            continue
    print(dic_t)

from itertools import permutations
def pert(x):
    t=permutations(x)
    lis_t=[]
    for i in t:
        lis_t.append(int("".join(i)))
        print(max(lis_t))


