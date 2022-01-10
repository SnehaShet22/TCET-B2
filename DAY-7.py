def merge_list(list1, list2):
    merged_data=""               #' '
    j = len(list1)-1             # 8 -1 = 7 
    for i in range(len(list1)): #1 2 3
        str1 = str2 = ''  # 
        if list1[i]:        #
            str1 =list1[i] # app' list[5]
        if list2[j]:
            str2 = list2[j] #'le
        j -=1                # 6 
        merged_data+=str1+str2 # An apple 
        if i < len(list1)-1 :
            merged_data+=' '
   
    return merged_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)


def mergelist(list1,list2):
    lenn = len(list2)-1
    mregedData = ''

    for i in range(0,len(list1)):
        if list1[i] == None:
            mregedData += list2[lenn]
        elif list2[lenn] == None:
            mregedData += list1[i] +" "
        elif list1[i]!= None and list2[lenn]!=None:
            mregedData += list1[i] + list2[lenn] +" "
        lenn -= 1

    print(mregedData)

list1 =  list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2= ['y','tor','e','eps','ay',None,'le','n']
mergelist(list1,list2)



class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

#Implement Service class here
class Service:
    def __init__(self,car_list) :
        self.__car_list = car_list 
    def get_car_list(self):
        return self.__car_list

    def find_cars_by_year(self ,year):
        list1=[] 
        for car in self.__car_list:
            if int(car.get_year()) == year:
                list1.append(car.get_model()) 
        if (len(list1)==0):
            return None
        return list1 

    def add_cars(self ,new_car_list):
        self.__car_list.extend (new_car_list) 
        self.__car_list.sort (key = lambda x : x.get_year()) 

    def remove_cars_from_karnataka(self):
        list1=self.__car_list.copy() 
        for car in list1:
            if car.get_registration_number()[0:2] == "KA":
                self.__car_list.remove(car) 

'''
def fun (x):
    x.get_year()

list1 = [1 , 2 , 3 , 4,[4,5,6],4 , 5 , 6]
list1.append ([4,5,6])
list1.extend([4,5,6])
'''


# [car1 , car2 ]

car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program




class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

#Implement Game class here
class Game :
    def __init__(self, players_list) :
        self.__players_list = players_list 
    
    def get_players_list(self):
        return self.__players_list

    def sort_players_based_on_experience(self):
        self.__players_list.sort(key = lambda x : Player.get_experience(x) , reverse=True)
        print(self.__players_list)

    def shift_player_to_new_position(self , old_index_position , new_index_position):
        old_index_position=old_index_position-1
        new_index_position= new_index_position-1 

        temp = self.__players_list[new_index_position]
        self.__players_list[new_index_position] = self.__players_list[old_index_position]
        self.__players_list[old_index_position] = temp 

        return self.__players_list

    def display_player_details(self):
        for i in range(len(self.__players_list)):
            print(Player.get_name(self.__players_list[i])) 
            print(Player.get_experience(self.__players_list[i])) 


#lambda x : Player.get_experience(x) 
#
# def fun( x):
#      Player.get_experience(x) 
#      return x 

player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
#Create object of Game class, invoke the methods and test your program
g = Game(players_list)
g.display_player_details()
print("**************************************************************")
g.sort_players_based_on_experience()
g.display_player_details()
print("**************************************************************")

g.shift_player_to_new_position(1 , 11)
g.display_player_details()

'''
temp = a 
a = b 
b = temp 
'''

#lambda x : Player.get_experience(x) 

#  def  fun (x):
#     return Player.get_experience(x) 
    

#lambda inp_value : expression 
'''
x = lambda a , b: a * b 

print(x(5, 6)) 

def fun (a , b):
    return a * b 

print(fun(5 , 6)) 
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


def create_new_sentence(word_list):
    new_sentence=""
    status = 0
    temp = word_list.get_head() 
    while (temp):
        ch = temp.get_data() # A 
        if ch=='/' or ch=='*':
            new_sentence += ' ' 
            if temp.get_next().get_data() == '/' or temp.get_next().get_data() == '*':
                status = 1
                temp = temp.get_next()
            temp=temp.get_next() 
            continue
        if status==1:
            ch = ch.upper() 
            status = 0
        new_sentence += ch 
        temp=temp.get_next() 
    return new_sentence 


word_list=LinkedList()
word_list.add("T")
word_list.add("h")
word_list.add("e")
word_list.add("/")
word_list.add("*")
word_list.add("s")
word_list.add("k")
word_list.add("y")
word_list.add("*")
word_list.add("i")
word_list.add("s")
word_list.add("/")
word_list.add("/")
word_list.add("b")
word_list.add("l")
word_list.add("u")
word_list.add("e")
result=create_new_sentence(word_list)
print(result)


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
        
class Child:
    def __init__(self,name,item_to_perform):
        self.__name=name
        self.__item_to_perform=item_to_perform

    def __str__(self):
        return(self.__name+" "+self.__item_to_perform)

    def get_name(self):
        return self.__name

    def get_item_to_perform(self):
        return self.__item_to_perform

class Performance :

    def __init__ (self,children_list):
        self.__children_list= children_list 

    def get_children_list(self):
        return self.__children_list
    
    def change_position(self , child):
        temp = self.__children_list.get_head()
        temp1 = self.__children_list.get_head()

        while temp.get_next():
            temp1=temp1.get_next() 
            if temp.get_next().get_next():
                temp = temp.get_next().get_next()
        self.__children_list.delete(child)
        self.__children_list.insert(child,temp1.get_data()) 

    def add_new_child(self,child):
        temp = self.__children_list.get_head()
        while temp.get_next():
            temp=temp.get_next()
        self.__children_list.insert(child,temp.get_data())
            


       
#Implement Performance class here
child1=Child("Rahul","solo song")
child2=Child("Sheema","Dance")
child3=Child("Gitu","Plays Flute")
child4=Child("Tarun","Gymnastics")
child5=Child("Tom","MIME")

#Add different values to the list and test the program
children_list=LinkedList()
children_list.add(child1)
children_list.add(child2)
children_list.add(child3)
children_list.add(child4)
children_list.add(child5)
performance=Performance(children_list)
print("The order in which the children would perform:")
performance.get_children_list().display()
print()
print("After Rahul's performance, the schedule would change to:")
performance.change_position(child1)
performance.get_children_list().display()
print()
child6=Child("Swetha","Vote of Thanks")
print("After Swetha has joined, the schedule is:")
performance.add_new_child(child6)
performance.get_children_list().display()

