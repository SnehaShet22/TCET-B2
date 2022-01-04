'''
def find_leap(year): 
    leap_year = []
    count = 0 
    while (count<15):
        if(year%400==0 or ( year% 4==0 and year %100!=0)):

            leap_year.append(year)            # [2000 , 2004 ]

            count += 1   # count = count + 1     0 1 2 

        year += 1    # year = year + 1           2004....
    return leap_year 

y = int(input()) 
leap_list = find_leap(y)
print(leap_list)


# list of gems and quantity
#Rs.30000 is entitled for 5% discount.
#not available in the store, then consider total bill amount to be -1.


def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    for gem in reqd_gems:
        if gem in gems_list:
            i1 = gems_list.index(gem)  # index of gem in gems list so that we can get price of that gem   # 1
            i2 = reqd_gems.index(gem)  #index of gem in required list so that we can get quantity of that gem # 0
            bill_amount= bill_amount+(reqd_quantity[i2]*price_list[i1])
            if bill_amount > 30000:         # 3   *  2119  + 10 * 
                bill_amount = bill_amount - ((bill_amount*5)/100)  # 5% discount 
        else:
            return -1 

    return bill_amount


#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]  

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)



def create_largest_number(number_list):
    number_list.sort(reverse=True) # desending order 
    s = '' 
    for i in number_list:
        s = s + str(i)    # s = '674523'
    return s
    
number_list=[23,45,67]
largest_number=create_largest_number(number_list) #674523
print(largest_number)

# [23 , 45 , 67 ] = [67 , 45 , 23]



def check_palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")


# word = Sejal 
# word[::-1] = lajeS
#                 -1
# [start : end : counter]     lajeS

# Sejal 



#AAAABBBBCCCCCCCCAAA = 4A4B8C3A


from typing import Counter


def encode(message):
    message= message + '0'   # AABCCA0
    t=''                     #t=''
    count=1 
    for i in range (len(message)-1): #7-1  6th element
        if message[i] == message[i+1]: # if element same as next element
            count+=1
        else:
            t = t + str(count) + message[i] 
            count = 1 
    return t 

encoded_message=encode("AABCCA") #2A1B2C1A
print(encoded_message)



child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    return sum(chocolates_received)  #total chocolates
                 # 20                   2
def reward_child(child_id_rewarded,extra_chocolates):
    if extra_chocolates < 1: 
        print("Extra chocolates is less than 1")
    elif child_id_rewarded not in child_id:
        print("Child id is invalid")
    else:
        i = child_id.index(child_id_rewarded)   # getting index of child id  = 1
        ch = chocolates_received[i] + extra_chocolates   # 5 + 2 = 7
        chocolates_received[i] = ch   # updating value of chocalates received 
        print (chocolates_received)   #[12,7,3,4,6]

   
print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2) 


''' 

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0

    if 1000<=account_number<1999:
        if account_balance>=100000:
            if salary>25000 and loan_type == 'Car':
                if loan_amount_expected<=500000 and customer_emi_expected <=36:
                    eligible_loan_amount=500000
                    bank_emi_expected=36
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")

            if salary>50000 and loan_type == 'House':
                if loan_amount_expected<=6000000 and customer_emi_expected <=60:
                    eligible_loan_amount=6000000
                    bank_emi_expected=60
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")

            if salary>75000 and loan_type == 'Business':
                if loan_amount_expected<=7500000 and customer_emi_expected <=84:
                    eligible_loan_amount=7500000
                    bank_emi_expected=84
                    print("Account number:", account_number)
                    print("The customer can avail the amount of Rs.", eligible_loan_amount)
                    print("Eligible EMIs :", bank_emi_expected)
                    print("Requested loan amount:", loan_amount_expected)
                    print("Requested EMI's:",customer_emi_expected)
                else:
                    print("The customer is not eligible for the loan")
            else:
                print("Invalid loan type or salary")
        else:
            print("Insufficient account balance")
    else:
        print("Invalid account number") 

        



            




    #Start writing your code here
    #Populate the variables: eligible_loan_amount and bank_emi_expected

    #Use the below given print statements to display the output, in case of success
    #print("Account number:", account_number)
    #print("The customer can avail the amount of Rs.", eligible_loan_amount)
    #print("Eligible EMIs :", bank_emi_expected)
    #print("Requested loan amount:", loan_amount_expected)
    #print("Requested EMI's:",customer_emi_expected)

    #Use the below given print statements to display the output, in case of invalid data.
    #print("Insufficient account balance")
    #print("The customer is not eligible for the loan")
    #print("Invalid account number")
    #print("Invalid loan type or salary")
    # Also, do not modify the above print statements for verification to work


#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)



'''
def find_common_characters(msg1,msg2):
    msg1= msg1.replace(' ','')
    msg2= msg2.replace(' ','')
    t ,s= '','' 
    for i in msg1:
        if i in msg2 :
            t=t+i 
    for i in t :
        if i not in s :
            s += i 
    return(s if s!='' else -1)

#Provide different values for msg1,msg2 and test your program
msg1="moto"
msg2="moto"   # moto #mot
common_characters=find_common_characters(msg1,msg2) #lieyon
print(common_characters)


vowels = ['a','e','i','o','u']
def encrypt_sentence(sentence):  #    0     1       2
    l = sentence.lower().split() # ['the', 'sun', 'rises', 'in', 'the', 'east']
    t = []
    for i in range(len(l)):
        if i%2==0:   #the[::-1] = eht 
            t.append(l[i][::-1]) 
        else:
            c , v = '','' 
            for j in l[i]:      # sun    s    u    n
                if j not in vowels:
                    c += j     # c will contain consonants  s n
                else:
                    v += j     # v will contain vowels      u

            t.append(c+v)   # snu 

    return ' '.join(t)

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence) #['eht', 'snu', 'sesir', 'ni', 'eht', 'stea']
print(encrypted_sentence)

 

def find_correct(word_dict):
    #start writing your code here
    correct = 0
    almost_correct = 0 
    wrong = 0 
    for k , v in word_dict.items():
        if k == v:
            correct+=1    # 2 
        else :
            if len(k)!= len(v):
                wrong +=1   # 1
                continue 
            c = 0
            for i in range (len(k)):
                if k[i] != v[i]: # how many letters are wrong
                    c += 1     # 1 2 
            if c <= 2 :
                almost_correct += 1   # 2
            else:
                wrong += 1
    return [correct,almost_correct,wrong]  # [2,2,1]
              
\'''
    k        v 
['THEIR', 'THEIR']
['BUSINESS', 'BISINESS']
['WINDOWS', 'WINDMILL']
['WERE', 'WEAR']
['SAMPLE', 'SAMPLE']
\'''




word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))





def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    l=[]
    for k in medical_speciality.items():  # P O E 
        count= patient_medical_speciality_list.count(k)  
        l.append(count) # [3 , 0 ,2]
    maximum= l.index(max(l))  # 0 
    speciality = tuple(medical_speciality.values())[maximum] #(Pediatrics ,Orthopedics ,ENT)[0]
    return speciality

#(Pediatrics ,Orthopedics ,ENT)
#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)


l = [56 , 86 ,72 ]
max(l)



def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    final = [0,0,0]
    o = 0
    p = 0
    e = 0
    for i in patient_medical_speciality_list:
        # print(i)
        if i == 'P':
            p+=1
            final.insert(0,p)

        elif i == 'O':
            o += 1
            final.insert(1,o)

        elif i == 'E':
            e +=1
            final.insert(2,e)

    maxx = max(final)
    id = final.index(maxx)
    if id == 0:
        return "Pediatrics"
    elif id == 1:
        return "Orthopedics"
    elif id == 2:
        return "ENT"

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)



vowels = ['a','e','i','o','u','A','E','I','O','U']
def sms_encoding(data):
    word = data.split()  #['I', 'love', 'Python']
    l = []
    for i in word :
        temp=[]
        for letter in i :
            if letter not in vowels:   #Python'
                temp.append(letter)     # [P,y,t,h,n] ''.join(t) = Pythn
        if len(temp)==0:
            temp.append(i)    #[]
        l.append(''.join(temp))  # l = [I ,lv ,pythn ]
    return ' '.join(l)   # I lv pythn

data="I love Python"
print(sms_encoding(data)) 
''' 

def max_frequency_word_counter(data):
    word=""
    frequency=0 
    raw = (data.lower()).split()
    temp,cnt, l ,length = [],[],[] ,[]
    ['work', 'like', 'you', 'do', 'not', 'need', 'money,', 'love', 'like', 'you', 'have', 
    'never','been', 'hurt,', 'and', 'dance', 'like', 'no', 'one', 'is', 'watching']
    for val in raw :
        if val not in temp:
            temp.append(val) # values without duplicates 
    
    ['work', 'like', 'you', 'do', 'not', 'need', 'money,', 'love', 'have', 'never',
     'been', 'hurt,', 'and', 'dance', 'no', 'one', 'is', 'watching']

    for i in temp :
        c=raw.count(i)  
        s1 = str(i)+' '+str(c)
        cnt.append(c) # storing count [0,1,1,3,3]
        l.append(s1)  # words with count 

    frequency = max(cnt) 
    if cnt.count(frequency)>1:
        for i in range(len(cnt)):
            if cnt[i] == frequency:
                length.append(len(l[i])) #checking length of word 
            m = max(length) 
            i1 = length.index(m)
            word=l[i1] 
            print(word)
    else:
        num = str(frequency)
        for i in l:
            s=i.split()
            for val in s :
                if num in val :
                    word=s[0]
        print(word,frequency)

data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data) #like 3