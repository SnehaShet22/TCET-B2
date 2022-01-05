def find_pairs_of_numbers(num_list,n):
    count = 0 
    for i in num_list: # i = 1 
        s = n - i      # s = 6 - 2 = 4     (1 , 5 ) , (2 , 4)    # n = s + i   s = n - i
        if s in num_list:
            count += 1   # 1  
    return count//2 

num_list=[1, 2, 4, 5, 6] 
n=6
print(find_pairs_of_numbers(num_list,n))




                               # even
def sum_of_numbers(list_of_num,ff=None):
    num_sum = 0 
    if ff!=None:
        num_sum=sum(ff(list_of_num))  # sum of (even(data)) # function call to even (returns list of even numbers)
    else:
        num_sum=sum(list_of_num)   # sum of range (1 , 11) 
    return num_sum
    
def even(data):
    even1 = [] 
    for i in data :
        if i%2==0:
            even1.append(i)
    return even1 

def odd(data):
    odd1 = []
    for i in data :
        if i%2!=0:
            odd1.append(i)
    return odd1


sample_data = range(1,11)

print(sum_of_numbers(sample_data,even))

 
def check_double(number):
    double = number * 2 
    if len(str(number)) == len(str(double)) :
        if set(str(number)) == set(str(double)) and number!=double:
            return True
        else:
            return False
    return False

print(check_double(125874))

"""
expenses = (distance/milage)* fuel cost
income = passenger * price of ticket 

"""

Pricefuel = 70
Mileage = 10
Priceicket = 80
#lex_auth_012693816779112448160

def calculate(distance,no_of_passengers):
    expenses = (distance/Mileage)*Pricefuel
    income = no_of_passengers * Priceicket
    if expenses < income:
        return income - expenses
    else:
        return -1

distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))


list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    avg = sum(list_of_marks)/ len(list_of_marks) 
    count = 0 
    for marks in list_of_marks:
        if marks>avg:
            count += 1 
    return ((count /10)* 100)                         # count  * 10
                                                      #        
def sort_marks():
    return sorted(list(list_of_marks))

def generate_frequency():
    l = [] 
    for i in range(0,26):
        l.append(list_of_marks.count(i))    # (12,18,25,24,2,5,18,20,20,21).count(2) =1
    return l 

print(find_more_than_average())
print(generate_frequency())
print(sort_marks()) 


list = []
tuple= () 


def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    list_of_factors.sort(reverse=True) 
    for fact in list_of_factors: #[1 ,2,3,]
        if is_prime(fact,fact//2):
            return fact
    return 1

def find_f(num):              #f(n)
    if is_prime(num,num/2): #(1 , num)
        return num 
    else:
        l = find_factors(num)   # 12
        return find_largest_prime_factor(l) # 3

def find_g(num):
    sum=0
    for i in range(num , num+9):
        sum=sum+find_f(i)     # g(n) = f(n) + f(n+1) + f(n+2) + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8)
    return sum
print(find_g(10)) 



def find_smallest_number(num):
    for value in range (1 , 1000):   # 6
        list=[] 
        for n in range(1,value+1): # 1 2 3 4 5 6
            if value%n==0:
                list.append(n)    #[1 2 3 6]

        if len(list) == num :
            return value
num= 4 
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)


def find_duplicates(list_of_numbers):
    temp=[]
    for i in list_of_numbers:
        if list_of_numbers.count(i) > 1 and i not in temp:
            temp.append(i)   # [2]
    return temp
 
list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)


def check_anagram(data1,data2):
    data1= data1.lower()
    data2=data2.lower()
    l1 , l2 = [] ,[]
    for index , v in enumerate(data1):
        l1.append((index , v))  #[(0, 'b'), (1, 'a'), (2, 'c'), (3, 'k'), (4, 'w'), (5, 'a'), (6, 'r'), (7, 'd')]
    print(l1)
    
    for index , v in enumerate(data2):
        l2.append((index , v))
    print(l2) 
    
    if len(l1) == len(l2) :
        if set(data1) == set(data2):  # data1 = tea {'t','e','a'}
            for i in l1 :              #data2 = eat {'t' , 'e','a'}
                if i in l2:
                    return False
            else:
                return True

        else:
            return False
    else:
        return False

print(check_anagram('backward','drawback'))


def find_duplicates(list_of_numbers):
    temp=[]
    for i in list_of_numbers:
        if i not in temp:
            temp.append(i)   # [1 ,2 , 3 , 4]
    return temp
 
list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)


'''
find factors of that number         factor of 6 = 1,2,3 = 1+2+3 = 6  
check sum of factors == number 
'''

def check_perfect_number(num):
    factors = []
    for i in range(1,(num)):
        if(num%i==0):
            factors.append(i)
    if sum(factors) == num:
        return True
    else:
        return False

def check_perfectno_from_list(no_list):
    perfectno = [] 
    for i in no_list:
        res= check_perfect_number(i) 
        if res==True:
            perfectno.append(i) 
    return perfectno


perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list) 

def nearest_palindrome(number):  # 12302.......12321
    number = number + 1
    for i in range(number,number+1000): # number =number
        if str(i)[::-1] == str(i):       
            return i 

number=12300 
print(nearest_palindrome(number)) 


import re 

def validate_name(name):
    if 0<len(name)<16:
        if str.isalpha(name):
            return True
    return False
    #Start writing your code here

def validate_phone_no(phno):
    if len(phno)==10:
        if str.isdigit(phno):
            for i in phno:
                if phno.count(i)!=10: # 9999999999 
                    return True
    return False
    #Start writing your code here

def validate_email_id(email_id):
    if re.search('@gmail.com$|@yahoo.com$|@hotmail.com$',email_id)!=None:
        if email_id.count("@")==1 and email_id.count('.com'==1):
            return True
    return False 

def validate_all(name,phone_no,email_id):
    if not validate_name(name):
        print("Invalid Name")
    if not validate_phone_no(phone_no):
        print("Invalid phone number")
    if not validate_email_id (email_id):
        print("Invalid email id")
    if validate_name(name) and validate_phone_no(phone_no) and validate_email_id(email_id):
        print("All the details are valid") 


#Provide different values for name, phone_no and email_id and test your program
validate_all("Tina", "9994599998", "tina@yahoo.com")



def validate_credit_card_number(card_number):
    card = str(card_number)
    l = [] 
    if len(card == 16):                #                         -4-3-2-1
        for i in card [-2::-2]:        # 4 5 3 9 8 6 9 6 5 0 1 3 3 1 0 1   
            n = int(i)*2
            if n > 9 :              # 18
                n1=n%10 + n//10     # 8 + 1 =
                l.append(n1)
            else:
                l.append(n)
        return(sum(l)+sum(list(map(int,card[-1::-2]))))%10 == 0
    else:
        return False
    
    #start writing your code here

card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")


#(sum(l)+sum(list(map(int,card[-1::-2]))))%10 == 0
#sum(l) = sum of 2nd last numbers
#sum(list(map(int,card[-1::-2])))) = sum of all remaining numbers 
