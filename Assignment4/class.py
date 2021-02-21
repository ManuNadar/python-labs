#mobile billing
class mobile_billing:
    bill = 0
    def __init__(self, time, sms,service):
       self.time = time
       self.sms = sms 
       self.service=service
      

       if self.service == 'Postpaid':
           self.callrate = 0.01
           self.smsrate = 1
       else:
           self.callrate = 0.005
           self.smsrate = 0.5

    def total_bill(self):

        self.bill += self.time * self.callrate + self.sms * self.smsrate 
        return self.bill

m1=mobile_billing(30,34,"Postpaid")
print(m1.total_bill())

Bank account class 
class Bank_account:

   def __init__(self, account_no, bal, withdrawl):
      self.account_no = account_no
      self.bal = bal
      self.withdrawl = withdrawl

      self.interest_rate = 0.06
      self.branch = "Modinagar"
 
   def credit(self, value):
      self.bal += value
 
   def debit(self, value):
      self.bal -= value
 
   def comp_int(self, n):
      self.bal *= (1+self.interest_rate)*n # n in years

   def __str__(self):
      return f"No.{self.account_no} with Total Balance(bal - withdrawl) = Rs.{self.bal - self.withdrawl}"
b1=Bank_account(99003711,25000,2000)
print(b1.__str__())


 
Color class
import webcolors
class color:
 
  def __init__(self, hex_value):
    self.red = hex_value[0]
    self.green = hex_value[1]
    self.blue = hex_value[2]
    self.hex_value = hex_value
 
  def form_color(self):
     try:
       return webcolors.rgb_to_name(self.hex_value)
     except ValueError:
       print("Invalide color code")
 

#Point class
class Point:

   def __init__(self, x, y):
      self.x = x 
      self.y = y 

   def quad(self): 
       if self.x > 0:
         if self.y > 0:
           return 1
         else:
           return 2
       else:
          if self.y > 0:
           return 3
          else:
            return 4
 
   def __str__(self):
      return f"({self.x}, {self.y})"
 
  
p1=Point(12,-2)
print(p1.__str__())




Class Circle/Rectangle/Triangle
class circle:
     def __init__(self, radius):
        self.radius = radius
 
     def circumference(self):
         return 2*3.141*self.radius
 
     def area(self):
         return 3.141 * (self.radius ** 2)



rectangle    

class rectangle():
    def __init__(self, a,b):
       self.a = a
       self.b = b

    def area(self):
      return self.a * self.b
 
    def circumference(self):
       return 2 * (self.a + self.b)


c3=rectangle(16,8)
print(c3.circumference())
print(c3.area())








#Class Box
class box:
    def __init__(self, len, br, he):
       self.len = len
       self.br = br
       self.he = he
 
    def volume(self):
       return self.len * self.br * self.he
 
    def display(self):
       print(f"Length = {self.len}, Breadth = {self.br}, Height = {self.he}")

b1=box(12,15,9)
print(b1.volume())
b2=box(12,16,18)
print(b2.display())

 
 
 class IP address

class ipaddress:
    def __init__(self, int_address):
       self.address = int_address

    def address_str(self):
        s = ""
        k = 3
        while k >=0:
            s += str((self.address // pow(256, k))%256) + "."
            k -= 1

        return s[:-1]

ip1=ipaddress(265)
print(ip1.address_str())



