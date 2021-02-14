#mean
'''def smaller_mean():
    count=0

    numbers=[20,30,40,50,60]
    length=len(numbers)
    numbers_sum=sum(numbers)
    mean=numbers_sum/length
    for i in  numbers:
        if i<mean:
            count+=1
        else:
            i+=1
    return count'''

#differance
'''def differance():
    list=[20,30,12,16,8,70]
    list.sort()
    print(list)
    a=list[0]
    b=list[1]
    diff=b-a
    return diff'''

#odd man out
'''def stray_num(l):
   
    
    length = len(l)
    i = 0
    st = l[0]
    for i in range (1,length):
        stray_number = st ^ l[i]
        
    return stray_number'''


# Find the missing number
'''def missing_no(l1,l2):
    li = []
    li = list(set(l1)-set(l2))

    return li'''

#no of people onboarding and alighting at eacg station
'''def res_people(list1,list2):

    i = 0
    s1 = 0
    s2 = 0
    rem_sum = 0
    for i in list1:
        s1 = s1 + i
    for i in list2:
        s2 = s2 + i    
    rem_sum= s1-s2
    
    prin
    
    return rem_sum'''

# Find the missing number, given the original list and modified one


'''def fin_no(l1,l2):
   fin_li = []
   fin_li = list(set(l1)-set(l2))

   return fin_li'''








