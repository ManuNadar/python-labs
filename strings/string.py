#correct  malformed time string
'''def corr_string(s):
    a = s.split(":")
    h = int(a[0])
    m = int(a[1])
    s = int(a[2])
    if s >= 60:
        new_s = s%60
        new_m = m + s//60
        m = new_m
    if m >= 60:
        new_m = m%60
        new_h = h + m//60
    print("{0}:{1}:{2}".format(new_h, new_m, new_s))


string = input()
corr_string(string)'''




#malformed date string
'''def corr_date(d):
    a = d.split("/")
    day = int(a[0])
    mon = int(a[1])
    year = int(a[2])
    O_mon = [1,3,5,7,8,10,11]
    Flag = True
    if day > 30 and mon not in O_mon:
        new_mon = mon + day//30
        new_day = day%30
        Flag = False
    elif day > 31 and mon in O_mon:
        new_mon = mon + day//31
        new_day = day%31
        Flag = False
    else:
        new_mon = mon

    if Flag and mon > 12:
        new_year = year + mon//12
        new_mon = mon%12
    elif not Flag and new_mon > 12:
        new_year = year + new_mon//12
        new_mon = new_mon%12
    else:
        new_year = year
        
    print("{0}/{1}/{2}".format(new_day, new_mon, new_year))

date = input()
corr_date(date)'''

#largest no by deleting single digit
'''def lar_num(num):
    for i in range(len(num)-1):
        if num[i] < num[i + 1]:
            num.remove(num[i])
            break
    s = ""
    for ele in num:
        s = s + str(ele)
    print(s)

n = input()
num = []
for ele in n:
    num.append(int(ele))
lar_num(num)'''


#generate accumulated string

''''def acc_string(s, alpha):
    ans = ""
    for i in range(len(s)):
        ans = ans + alpha[s[i]] + s[i]*i + "-"

    print(ans[:len(ans)-1])

s = input()
alpha_dict = {
    'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F', 'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'x':'X', 'y':'Y', 'z':'z'
    }
acc_string(s, alpha_dict)''''

