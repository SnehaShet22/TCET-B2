'''
arrival_time_list = departure_time_list
600    1110        5 -1 = 4
800,    1130
850,    1200 
900     1400
1050    1700
1120    650

hint:
sort both list 
iterate through both list 
if arrival < departure 
platform + 1 
if departure < arrival 
platform - 1 
if arival == departure 
no changes 


def find_number_of_platforms(arrival_time_list,departure_time_list):
    arrival_time_list.sort()
    departure_time_list.sort() 
    n = len(arrival_time_list) 

    plat_needed = 1 
    result = 1 
    i = 1 
    j= 0

    while (i<n and j < n):
        if (arrival_time_list[i] < departure_time_list[j]):
            plat_needed +=1 
            i +=1
        
        elif (arrival_time_list[i] > departure_time_list[j]):
            plat_needed -=1 
            j +=1 
        
        if plat_needed > result:
            result = plat_needed
 
    return result


#Pass different values to the function and test your program
arrival_time_list = [800,850,600,1120,1050,900]
departure_time_list = [1110,1200,1400,1130,1700,2200]
print("The arrival time of the trains:", arrival_time_list)
print("The departure time of the trains:",departure_time_list)
print("Minimum number of platforms required :",find_number_of_platforms(arrival_time_list,departure_time_list))
'''
'''
n = 00000
'''

#n = 5 4 3 2 1 0

'''
a[n] = a[n-1] + b [n-1] a ends with 0   = 00 01
b[n] = a [n-1]          b ends with 1   = 10 

'''

def count_strings(number):
    a = [ 0 for i in range (number)] # 1 2 3
    b = [0 for i in range(number)]  #  1 1  2
    a[0] = b[0] = 1 
    for i in range(1 , number):
        a[i] = a [i-1] + b [i-1]
        b[i] = a[i-1] 

    return a[number-1] + b[number-1] 


#Pass different values to the function and test your program
number=5
print("The number of strings that can be made are:",count_strings(number))


def find_unknown_words(text, vocabulary):
    # Remove pass and write your logic here
    list = text.split(" ") #[The ,sun, rises, in ,the, east, and, sets, in, the, west.]
    final_set=set()        # set(and , sets ,west)
    set1 = set(list)       # {The ,sun, rises , in , east , and , sets , west }
    set2 = set(vocabulary) #  {"sun","in","rises","the","east"}
    for i in set1:
        if i not in set2:
            final_set.add(i)
    if final_set:
        return final_set
    else:
        return -1

text='coffee is hot'
vocabulary = ["hot"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)

def find_unknown_words(text, vocabulary):
    text = (text.split(' ')) 
    s = set() 
    for i in text :
        if i not in vocabulary :
            s.add(i) 
    if s :
        return s 
    else:
        return -1 

'''
       20
  8         22
4   12

20 
8 22 
4 12 
'''
'''
class newNode :
    def __init__(self , data):
        self.val = data 
        self.left = None
        self.right = None 

def printLevelOrder(root):
    if root is None:
        return 
    q = []       # []
    q.append(root) 

    while q : # []
        count = len(q) # 3

        while count> 0 :
            temp = q.pop(0)   # temp = 6
            print(temp.val , end = ' ')  # 1 2 3 4 5 6
            if temp.left :      #   
                q.append(temp.left) 
            if temp.right :     # [ ]
                q.append(temp.right) 
            count -= 1          # 0
        print(' ') 

root = newNode(1) 
root.left = newNode(2) 
root.right = newNode(3) 
root.left.left = newNode(4) 
root.left.right = newNode(5) 
root.right.right = newNode(6) 

printLevelOrder(root)
'''
'''
     1
  2    3
4   5    6

print nodes at k distance 2 = 4 5 6 

'''
class newNode :
    def __init__(self , data):
        self.data = data 
        self.left = None
        self.right = None 
def printKDistant(root , k): #(root=3 ,1) (root = 6 ,0)
    if root is None:
        return
    if k == 0 :
        print(root.data , end = ' ') # 4 5 6 
    
    else:
        printKDistant(root.left , k-1) # 
        printKDistant(root.right , k-1)# 

root = newNode(1) 
root.left = newNode(2) 
root.right = newNode(3) 
root.left.left = newNode(4) 
root.left.right = newNode(5) 
root.right.right = newNode(6) 

printKDistant(root , 2)
