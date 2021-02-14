'''def greater(a, b, c):

    if a >= b and a >= c: 
        return a

    elif b>= a and b >= c: 
        return b

    else:
      return c'''

#armstrong   
'''def armstrong(x):

    sum = 0

    temp = x



    while temp > 0:

      rem = temp % 10

      sum += rem**3

      temp = temp//10

    if x== sum: 
        return 1

    else:

      return 0'''

#rev of a number
'''def rev(num):
    rev=0
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+rem
        rev=rev*10+rem
        num=num//10
        print("rev of a no",rev)
        print("sum of no",sum)'''

#GCD
'''def gcd(x, y) :

    while (x != y):

       if x > y:

         X = X-y

       else:

         y = y-x

         return x'''

#LCM
'''def lcm(a, b):

    bigger_no = 0

    if(a> b):

       bigger_no = a

    else:

      bigger_no =b



      while(True):

        if (bigger_no % a == 0 and bigger_no % b == 0):
            lcm = bigger_no

        break

    bigger_no=bigger_no+1
    return lcm'''

#leap yr
'''def leap(yr):

   flag = 0

   if(yr % 400 == 0):

     flag = 1

   elif(yr % 100 == 0):

     flag = 0

   elif(yr % 4 == 0):

     flag = 1

   else:

     flag = 0

   return flag'''

#triangles
'''def triangle_type (a, b, c):

  if(a+b >= c or b+c >= a or c+a >= b):
      print("triangle")

      if(a == b == c):

        print ("equilateral traingle")

      elif (a == b or b == c or c == a): 
        print ("isosceles traingle")

      elif((a*a ==(c*c+b*b) **0.5) or (b*b==(a*a+c*c)**0.5)):


        print ("right traingle")

      else:

        print("scalene traingle")

  else:

    print("NOT a valid traingle")'''

#roots
'''def find_root (a, b, c):

  

      d= b*b-4*a*c

      if(d > 0):

        root1 =(-b+d**.5)/2*a

        root2 = (-b-d**.5)/2*a

        print ("Uniq roots are : ", root1, root2)

      elif(d ==0):

          root1 = root2= (-b/2)*a

          print ("both are same roots :", root1, root2)
      else:

          real = -b/2*a

          img = (-d)**.5/2*a

          print ("Real and imaginary roots are :", real, img)'''

#triangular number
'''def triangular_num(n):
    sum = 0
    i = 0
    j = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum = sum + j
    return sum'''


  #del digit
'''def del_digit(num):
      x= 0
      i = 1
      while (num//i > 0):
        t=(num//(i*10))*i+(num%i)
        i = i*10
        if t>x:
            x=t
        return x '''

#super prime
'''def super_prime(x):
    count = 0
    i = 0
    list = []
    for i in range (2,x+1):
        flag = 0
        for j in range (2,i):
            if(i%j == 0):
                flag = 1
                break
        
        if(flag == 0):
            list.append(i)
            count = count+1         

    for i in range (2,count):
        flag = 0
        for j in range (2,i):
            if(i%j == 0):
                flag = 1
                break
        
        if(flag == 0):
            print(list[i])'''

#combinations
'''def combination(num):
    return(ft(num)/(ft(num-2)*ft(2)))

def ft(num):
    fact = 1
    i = 0
    for i in range(1,num+1):
        fact = fact*i
    return fact '''



#quardranrt
'''def quad(a, b):
  if(a == 0 and b == 0):
    return 0
  elif(a> 0 and b > 0):
    return 1
  elif(a < 0 and b < 0):
    return 2
  elif(a > 0 and b< 0):
    return 3
  else:
      return 4'''

#arithmetic 
'''def arithmetic(a,b):
    print("add:,1")
    print("sub:,2")
    print("mul:,3")
    print("mod:,4")
    print("div:,5")
    print("expo:6")
    ch=int(input("enter choice"))
    if ch==1:
      return a+b
    elif ch==2:
      return a-b
    elif ch==3:
      return a*b

    elif ch==4:
      return a%b

    elif ch==5:
      return a/b
    elif ch==6:
      return a**b
    else:
      print("invalid input")'''

#tribonacci series
'''def fibo(n):
  list=[0,0,1]
  for i in range(3,n):
    list.append(list[i-1]+list[i-2]+list[i-3])
  return list'''

#factorial
'''def factorial(n):
  fact=1
  while n>0:
    fact=fact*n
    n=n-1
  return fact'''
#vowl check
'''def vowel_ch(ch):
  if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')): 
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
      print("vowel")
    else:
      print("consonent")'''


#digital root

'''def digital_root(num):
    while num>num:
      sum=0
      for i in str(num):
        sum=sum+int(i)
        num=sum
      return sum'''


#prime no in range
'''def prime_number(ur,lr):
  for i in range(ur, lr+1): 
    if i>1: 
      for j in range(2,i): 
        if(i % j==0): 
          break
        else: 
         print(i)'''

# some of factor

''''def factor_sum(num):
    sum = 0
    i=1
    while(i < num):
        if(num%i == 0):
            
            sum = sum + i
        i = i+1
    return sum'''


