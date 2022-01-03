'''
def find_product(num1 , num2 , num3):
    product = 0 

    if (num1!=7 and num2!=7 and num3!=7):   # check for all numbers
        product=num1*num2*num3 
    
    elif (num1==7 and num2!=7 and num3!=7): #check for num1
        product= num2 * num3 

    elif (num1!=7 and num2==7 and num3!=7):#check for num2
        product=num3 
    
    else:                                 ##check for num3
        product = -1 
    return product 

product = find_product(7,7,8)
print(product)  

Three numbers can be the sides of a triangle if none of the numbers are greater than or equal to the sum of the other two numbers.

num1 < num2 + num3 

num2 < num1 + num3

num3 < num1 + num2

all 3 are true then it will form a triangle 



def form_triangle(num1 , num2 , num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    a = num1 + num2 
    b = num1 + num3
    c = num2 + num3 

    if num1 < c  and num2 < b and num3 < a :
        return success
    else:
        return failure

num1=3                   
num2=2
num3=5
s = form_triangle(num1, num2, num3) 
print(s)


total = 2 + 20 = 22 
sk = 21  4  1


11+10 = 21 
11  2 1

3+15 = 18


                               # how much we have
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    five_needed = int(rupees_to_make /5) 
    one_needed = int(rupees_to_make % 5)

    if five_needed <= no_of_five and one_needed<=no_of_one:  # check if we have amount
        print("No. of Five needed :", five_needed)   # how much to give to shopkeeper
        print("No. of One needed  :", one_needed)

    elif five_needed> no_of_five:          # check if we have less a
        total = no_of_five * 5
        one_needed = rupees_to_make - total 
        if one_needed <= no_of_one:
            print("No. of Five needed :", no_of_five)
            print("No. of One needed  :", one_needed)

        else:
            print(-1)
    else:
        print(-1)


make_amount(28,8,5) 







def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    amt = 0 
    #write your logic here
    if quantity_ordered > 0 and distance_in_kms>0 :
        if food_type == 'n' or food_type == 'v':
            return -1 
        if food_type == 'N':
            amt = 150
        elif food_type == 'V':
            amt = 120 
        
        bill_amount = amt * quantity_ordered 
        if distance_in_kms< 4:
            dist_amt = 0 
            bill_amount+=dist_amt
        elif 3<= distance_in_kms<=6: 
            dist_amt = (distance_in_kms-3)*3
            bill_amount+=dist_amt
        else:
            dist_amt1 = ((distance_in_kms-6)*6)+9
            bill_amount+=dist_amt1 
    else:
        bill_amount=-1
    return bill_amount


#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)

'''

def find_max(num1, num2):
    max_num=-1 

    l = [max_num] 
    if num1 < num2:
        for i in range (num1 , num2+1):    
            if len(str(i)) == 2:
                if i%3 == 0:
                    if i%5 == 0:
                        l.append(i) 
    return max(l)


# divisible by 3 = 99 = 9+9 = 18 divisible

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)



def find_max(num1, num2):
    max_num=-1 

    l = [max_num] 
    if num1 < num2:
        for i in range (num1 , num2+1):    #for i in range (0 , 10+1) : 0 1 ....9 10
            if len(str(i)) == 2:
                sum = 0 
                for num in str(i):        # 334
                    sum=sum+int(num)      # 13
                if sum%3==0:
                    if i%5==0:
                        l.append(i)
    return max(l)


# divisible by 3 = 99 = 9+9 = 18 divisible

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)


                #start    # end
#for i in range (0 ,       10+1) :
#0 1 2 3 4 5 6 7 8 9 10


def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0


    if heads == (legs//2):     # checking for chicken heads
        chicken_count = heads 

    elif heads == (legs//4):     # checking for rabbit heads
        rabbit_count = heads 

    elif legs%2==0:             # check for both chicken and rabbit
        rabbit_count = (legs//2) - heads 
        chicken_count = heads - rabbit_count

    else:
        print(error_msg)
    
    if chicken_count > 0 or rabbit_count > 0:
        if chicken_count<=heads and rabbit_count<=heads:
            print(chicken_count,rabbit_count)
        else:
            print(error_msg)

solve(38,131)
'''
head = 38 
leg = 130

chicken_count = 65
rabbit_count = 32


rabbit_count = 65 - 38 = 27
chicken_count = 38 - 27 = 11
'''


# HOW TO CHECK IF NUMBER IS PALINDROME 
'''
input num 
temp = num   123
reverse = 0 

while (number!=0):
    remainder = num % 10              3   2  1      
    reverse = reverse*10 + remainder  321
    num = num/10                     12  1  0 
end while 

if temp==reverse then
display 'it is palindrome 
else
display not palindrome
end if 

123
'''

