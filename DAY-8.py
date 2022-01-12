class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail


    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list")

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


def remove_duplicates(duplicate_list):
    #write your logic here
    temp = duplicate_list.get_head()         # 30 40 40 40 40
    while(temp.get_next()):
        if temp.get_data() == temp.get_next().get_data():
            temp1 = temp 
            temp = temp.get_next() 
            duplicate_list.delete(temp1.get_data()) 
            continue 
        temp = temp.get_next() 
    duplicate_list.display()
    return duplicate_list




#Add different values to the linked list and test your program
duplicate_list=LinkedList()
duplicate_list.add(30)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)
duplicate_list.add(40)

remove_duplicates(duplicate_list)

'''
def remove_duplicate(head):
    temp=head
    while temp.get_next() :
        if temp.get_data()==temp.get.next().get_data():
            temp.get_next()=temp.get_next().get.next()
        else:
            temp=temp.get_next()
    return head
''' 

class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail


    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list")

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

class BakeHouse:
    def __init__(self):
        self.__occupied_table_list=LinkedList()

    def get_occupied_table_list(self):
        return self.__occupied_table_list
    
    def allocate_table(self):
        for i in range(1,11):   # 1 3 4 5 
            if not self.__occupied_table_list.find_node(i): 
                self.__occupied_table_list.add(i) #2 
                break
        l=[]  # 1 3 4 5 2
        temp = self.__occupied_table_list.get_head()      # 1 3 4 5  2=none
        while(temp):
            l.append(temp.get_data())                      # 1 3 4 5 2
            temp= temp.get_next()             # h        t 
        l.sort()  # 1 2 3 4 5                 # 1  2  3  4
                                              # a2 a3 a4  n 
        self.__occupied_table_list=LinkedList()
        for value in l :
            self.__occupied_table_list.add(value) 

    def deallocate_table(self , table_number):
        temp = self.__occupied_table_list.find_node(table_number)
        if temp:
            self.__occupied_table_list.delete(temp.get_data())

bakehouse=BakeHouse()
#Invoke the methods of BakeHouse class and test the program


for i in range (1,10):
    if i==6:
        break
    else:
        print(i)
print('hii')

for i in range (1,10):
    if i==6:
        continue
    else:
        print(i)
print('hii')



class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next_node):
        self.__next=next_node


class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail


    def add(self,data):
        new_node=Node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node

    def insert(self,data,data_before):
        new_node=Node(data)
        if(data_before==None):
            new_node.set_next(self.__head)
            self.__head=new_node
            if(new_node.get_next()==None):
                self.__tail=new_node

        else:
            node_before=self.find_node(data_before)
            if(node_before is not None):
                new_node.set_next(node_before.get_next())
                node_before.set_next(new_node)
                if(new_node.get_next() is None):
                    self.__tail=new_node
            else:
                print(data_before,"is not present in the Linked list")

    def display(self):
        temp=self.__head
        while(temp is not None):
            print(temp.get_data())
            temp=temp.get_next()


    def find_node(self,data):
        temp=self.__head
        while(temp is not None):
            if(temp.get_data()==data):
                return temp
            temp=temp.get_next()
        return None

    def delete(self,data):
        node=self.find_node(data)
        if(node is not None):
            if(node==self.__head):
                if(self.__head==self.__tail):
                    self.__tail=None
                self.__head=node.get_next()
            else:
                temp=self.__head
                while(temp is not None):
                    if(temp.get_next()==node):
                        temp.set_next(node.get_next())
                        if(node==self.__tail):
                            self.__tail=temp
                        node.set_next(None)
                        break
                    temp=temp.get_next()
        else:
            print(data,"is not present in Linked list")

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
            msg.append(str(temp.get_data()))
            temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg

def reverse_linkedlist(reverse_list):
    l=[]  # 1 3 4 5 2
    temp = reverse_list.get_head()      # 1 3 4 5  2=none
    while(temp):
        l.append(temp.get_data())                      # 1 3 4 5 2
        temp= temp.get_next()
    l = l[::-1]  # reversed my list 
    reverse_list = LinkedList() 
    for value in l :
            reverse_list.add(value)  
    #write your logic here
    return reverse_list

#Add different values to the linked list and test your program
reverse_list=LinkedList()
reverse_list.add(10)
reverse_list.add(15)
reverse_list.add(14)
reverse_list.add(28)
reverse_list.add(30)


def reverse_List(self):
        prev_node = None                        # 10 15 14 28 30
        current_node = self.head                # 10
        while current_node is not None:
            next_node = current_node.next     # 14           15 10
            current_node.next = prev_node     #              a10 n
            prev_node = current_node
            current_node = next_node
        self.head = prev_node 



class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

def merge_queue(queue1,queue2):
    queue3 = Queue(queue1.get_max_size()+queue2.get_max_size())  
    l = queue1.get_max_size()+queue2.get_max_size()  # l = 6
    print(l) # 9 
    for i in range(l): # 0 1 2 3 4 5
        if not queue1.is_empty(): # 3 6 8
            queue3.enqueue(queue1.dequeue())
        if not queue2.is_empty(): # b y u t r o 
            queue3.enqueue(queue2.dequeue())
    mearged_queue = queue3   # 3 b 6 y 8 u t r o   
    return merged_queue 

#Enqueue different values to both the queues and test your program

queue1=Queue(3)
queue2=Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merged_queue=merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merged_queue.display()
                                # rear=
                                # front=0                  
# ticket counter 0 =             Dimple         data= Pravin

# QUEUE : FIRST IN FIRST OUT 
# isfull : if rear == max-1
# isempty : if front > rear
# if only one ele : front == rear
#enqueue = add
#dequeue = remove 


'''
newqueue = size of original queue 
while queue n ot empty 
ele = dequeue 
for i in range ( 0,11):
    check if element is not divisible by all
    break 
    else 
       add it in queue 
return queue
'''


#lex_auth_0127439130519060481634

class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

#Implement Job, Employee and Company classes here
class Job:
    def __init__(self,name , time_needed) :
        self.__name = name
        self.__time_needed = time_needed
        self.__time_elapsed = 0 
    def get_name(self):
        return self.__name
    def get_time_needed(self):
        return self.__time_needed
    def get_time_elapsed(self):
        return self.__time_elapsed

    def elapsed_time(self , no_of_mins):
        self.__time_elapsed += no_of_mins 
        if self.__time_elapsed>=self.get_time_needed:
            return True
        else:
            return False

class Employee:
    def __init__(self,name) :
        self.__name = name 
        self.__allocated_job = None
    def get_name(self):
        return self.__name
    def get_allocated_job(self):
        return self.__allocated_job

    def set_allocated_job(self , allocated_job):
        self.__allocated_job = allocated_job

    def elapsed_time(self , no_of_mins):
        if self.__allocated_job.elapsed_time(no_of_mins):
            job = self.__allocated_job
            self.__allocated_job=None
            return job
        else:
            return None 

class Company:
    def __init__(self,emp_list):
        self.__employees = emp_list
        self.__pending_jobs = Queue(10)
    def get_employees(self):
        return self.__employees
    
    def get_pending_jobs(self):
        return self.__pending_jobs

    def allocate_new_job(self , job):
        status=0
        for employee in self.__employees:
            if not employee.get_allocated_job():
                employee.set_allocated_job(job) 
                status=1
                break
        if status==0:
            self.__pending_jobs.enqueue(job)
        
    def elapsed_time(self,no_of_mins):
        completed_jobs=[]
        for employee in self.__employees:
            job = employee.elapsed_time(no_of_mins)
            if job:
                completed_jobs.append(job) 
                if(not self.__pending_jobs.is_empty()):
                    employee.set_allocated_job(self.__pending_jobs.dequeue()) 
            if len(completed_jobs)>0:
                return completed_jobs
            else:
                return None

                
    









#Change the values and test your programH

emp1=Employee("Ken")
emp2=Employee("Henry")
emp3=Employee("Jack")
emp4=Employee("Hen")
emp5=Employee("Jill")
emp_list=[emp1,emp2,emp3,emp4,emp5]
company=Company(emp_list)
job1=Job("job1",50)
job2=Job("job2",45)
job3=Job("job3",35)
job4=Job("job4",400)
job5=Job("job5",30)
job6=Job("job6",30)
job7=Job("job7",50)
job8=Job("job8",25)
company.allocate_new_job(job1)
company.allocate_new_job(job2)
company.allocate_new_job(job3)
company.allocate_new_job(job4)
company.allocate_new_job(job5)
company.allocate_new_job(job6)
company.allocate_new_job(job7)
company.allocate_new_job(job8)
print("Initial allocation:")
for emp in company.get_employees():
    print(emp.get_name(),"is allocated",emp.get_allocated_job().get_name())
print()
print("Pending Jobs:")
company.get_pending_jobs().display()
completed_jobs=company.elapsed_time(30)
'''print("Completed Jobs :")
for job in completed_jobs:
    print(job.name)'''

print("After completion:")
for emp in company.get_employees():
    print(emp.get_name(),"needs", emp.get_allocated_job().get_time_needed()-emp.get_allocated_job().get_time_elapsed(),"more minutes for",emp.get_allocated_job().get_name())
    print()
print("Pending Jobs:")
company.get_pending_jobs().display()
completed_jobs=company.elapsed_time(10)
print("After completion:")
for emp in company.get_employees():
    print(emp.get_name(),"needs", emp.get_allocated_job().get_time_needed()-emp.get_allocated_job().get_time_elapsed(),"more minutes for",emp.get_allocated_job().get_name())
    print()
print("Pending Jobs:")
company.get_pending_jobs().display()


class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg
        
        
def change_smallest_value(number_stack):
    l = [] 
    while (not number_stack.is_empty()):  #
        l.append(number_stack.pop())      # 5 66 5 8 7 
    mini = min(l)                         # 5
    counter = l.count(mini)               # 2 
    for i in range(counter): #(0,2) 0 1 2
        number_stack.push(mini)          # 5 5
    for element in l[::-1]:              # 7 8 5 66 5 
        if element!= mini:               # 
            number_stack.push(element)   # 5 5 7 8 66 
    return number_stack

#Add different values to the stack and test your program
number_stack=Stack(8)
number_stack.push(7)
number_stack.push(8)
number_stack.push(5)
number_stack.push(66)
number_stack.push(5)
print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display() 


'''
stack = last in first out 
top = -1 (initial) 
isfull = top==max-1
isempty = top==-1 
push = check if not full _ increment top _ add data 
pop = check if not empty _ data= pop data _ deccrement top 
'''


"""*********************Queue*****************************"""
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

"""*********************Stack*****************************"""
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg


def separate_boxes(box_stack):
    #Remove pass and write your logic here
    box_colour = ['Red','Green','Blue']
    l = box_stack.get_max_size()
    stack = Stack(l)
    queue = Queue(l) 
    while (not box_stack.is_empty()):
        color = box_stack.pop()          #
        if color.title() in  box_colour:
            stack.push(color)            # 
        else:
            queue.enqueue(color)         # purple white orange  yellow  magenta
    while (not stack.is_empty()):
        box_stack.push(stack.pop())      #  red  red green 
    return queue

#Use different values for stack and test your program
box_stack=Stack(8)      #red red  green 
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result=separate_boxes(box_stack)
print()
print("Boxes in the stack after modification:")
box_stack.display()
print("Boxes in the queue:")
result.display()




def find_matches(country_name):
    l = [] 
    for match in match_list:  #"AUS:CHAM:5:2"
        detail = match.split(':') # [AUS , CHAM , 5 , 2]
        if detail[0] == country_name:
            l.append(match)
    return l

def max_wins():
    dictionary = {}
    for match in match_list:  #"AUS:CHAM:5:2"     "AUS:WOR:2:1"
        detail = match.split(':') # [AUS , CHAM , 5 , 2] [AUS , WOR , 2 , 1]["ENG, WOR ,2, 0"]
        if detail[1] not in dictionary.keys():  # {CHAMP :2,WOR : 1 }
            dictionary[detail[1]]= None
        if dictionary[detail[1]]== None:
            dictionary[detail[1]]= int(detail[3]) 
        if dictionary[detail[1]]>= 0:
            if dictionary[detail[1]] < int(detail[3]) :
                dictionary[detail[1]]= int(detail[3]) 
    temp = dictionary.copy()                   # {CHAMP : 2,WOR : 1 }
    for key in dictionary.items():
        dictionary[key]=[]                      # {CHAMP :[ AUS ] , WOR :[AUS]}
    for match in match_list:  #"AUS:CHAM:5:2" "AUS:WOR:2:1"
        detail = match.split(':') # [AUS , CHAM , 5 , 2]  [AUS , WOR , 2 , 1]
        if int(detail[3])==temp[detail[1]]:
            dictionary[detail[1]].append(detail[0])  # dictionary[CHAM]=[AUS] 
    return dictionary 



def find_winner(country1,country2):
    count1 , count2 = 0 , 0 
    for match in match_list:  #"AUS:CHAM:5:2"
        detail = match.split(':') # [AUS , CHAM , 5 , 2] 
        if detail[0] == country1:
            count1 += int(detail[3])
        if detail[0] == country2:
            count2 += int(detail[3]) 
        if count1==count2:
            return 'Tie'
        elif count1>count2:
            return country1
        else:
            return country2


match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]


print("The match status list details are:")
print(match_list)
print()




def find_matches(country_name):
    #Remove pass and write your logic here
    pass

def max_wins():
    #Remove pass and write your logic here
    pass

def find_winner(country1,country2):
    #Remove pass and write your logic here
    pass

#Consider match_list to be a global variable
match_list=["AUS:CHAM:5:2","AUS:WOR:2:1","ENG:WOR:2:0","IND:T20:5:3","IND:WOR:2:1","PAK:WOR:2:0","PAK:T20:5:1","SA:WOR:2:0","SA:CHAM:5:1","SA:T20:5:0"]

#Pass different values to each function and test your program
print("The match status list details are:")
print(match_list)
print()



def last_instance( num_list,  start,  end,  key):
    count , index = 0,0
    if key in num_list:
        index=num_list.index(key) # 6
    if index:
        count = num_list.count(key)  # 4
    return index+count-1   # 10-1 = 9 

num_list=[1,1,2,2,3,4,5,5,5,5]
start=0
end=len(num_list)-1
key=5 #Number to be searched
#Pass different values for num_list, start,end and key and test your program
result=last_instance(num_list, start,end,key)

if(result!=-1):
    print("The index position of the last occurrence of the number:",result)
else:
    print("Number not found")


'''
mearge stack ()
create empty list 
while stack 1 not empty or stack2 not empty
add data in list 
sort list 
create new stack and push data of list into new stack 
'''

def count_decoding(digit_list):
    n = len(digit_list)

    count = [0]*(n+1)   # [1 , 1 , 0 , 0 , 0]
    count[0]=1
    count[1]= 1 

    for i in range(2 , n+1):
        count[i] = 0 
        if (digit_list[i-1]>0):
            count[i] += count[i-1] 
        
        if (digit_list[i-2]==1 or (digit_list[i-2]==2 and digit_list[i-1]<7)):
            count[i] += count[i-2]

    return count[n]

"""
1 -26 
1 (1 to 9)  2 (1 to 6)
"""


#Pass different values to the function and test your program
digit_list=[1 ,2 ,2 ,4]# [9 , 8 , 0 , 5]
print("Number of possible decodings for the given sequence is:",count_decoding(digit_list))


