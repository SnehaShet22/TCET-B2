#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count 

def find_passengers_destination(destination):
    count = 0 

    for i in ticket_list:
        string_list = i.split(':') 
        if (string_list[2] == destination):
            count +=1 
    return count
    #Write the logic to find and return the number of passengers traveling to the specified destination
    
    #Remove pass and write your logic here

def find_passengers_per_flight():
    l,m ,temp=[],[],[]
   
    for i in ticket_list:
        string_list = i.split(':')  # AI567,MUM,MUM,014  [AI567 ,MUM ,MUM , 014]
        if string_list :
            l.append(string_list[0])
    for i in l :
        if i not in temp: 
            temp.append(i) 
    for i in temp :
        s1 = l.count(i)
        s2 = str(i) + ':' + str(s1) #[AI077:4, BA896:6 ]
        m.append(s2)
    return m


def sort_passenger_list():
    l = find_passengers_per_flight()  #[AI077:4, BA896:6 ]
    temp = []
    final = [] 
    for i in l:
        s = i.split (':')  #[AI077,4]
        temp.append(s[1]) 
    temp.sort(reverse=True) #Descending order 
    for i in range (0 , len(temp)):
        for val in l:
            s2=val.split(':') # #[AI077,4]
            if temp[i] in s2:
                final.insert(i,val)
                break
    return final




#Provide different values for airline_name and destination and test your program.


print(sort_passenger_list())

final = [ 0 , 0 , 0 , 0]
final.insert(1,1000)   # [0, 1000, 0, 0, 0]
print(final)
final.append(5)   


######################################################################################

class Vehicle: 
    def __init__(self ) :
       self.__vehicle_cost = None
       self.__vehicle_id = None
       self.__vehicle_type = None
       self.__premium_amount = None 
    
    def set_vehicle_id(self , vehicle_id):
        self.__vehicle_id = vehicle_id
    def get_vehicle_id(self):
        return self.__vehicle_id 


    def set__vehicle_type(self , __vehicle_type):
        self.__vehicle_type = __vehicle_type
    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_cost(self , vehicle_cost):
        self.__vehicle_cost= vehicle_cost
    def get_vehicle_cost(self):
        return self.__vehicle_cost 

    def set_premium_amount(self , premium_amount):
        self.__premium_amount = premium_amount
    def get_premium_amount(self):
        return self.__premium_amount




'''
def check_type(type):
    vehicle_type=['Two Wheeler','Four Wheeler']
    if type not in vehicle_type:
        return 0
    return 1 

class Vehicle: 
    def __init__(self ) :
       self.__vehicle_cost = None
       self.__vehicle_id = None
       self.__vehicle_type = None
       self.__premium_amount = None 
    
    def set_vehicle_id(self , vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self.__vehicle_id 


    def set__vehicle_type(self , __vehicle_type):
        self.__vehicle_type = __vehicle_type

    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_cost(self , vehicle_cost):
        self.__vehicle_cost= vehicle_cost

    def get_vehicle_cost(self):
        return self.__vehicle_cost 

    def set_premium_amount(self , premium_amount):
        self.__premium_amount = premium_amount

    def get_premium_amount(self):
        return self.__premium_amount

    def calculate_premium(self):
        if self.__vehicle_type == 'Two Wheeler':
            self.__premium_amount = self.__vehicle_cost*2/100
        elif self.__vehicle_type == 'Four Wheeler':
            self.__premium_amount = self.__vehicle_cost*6/100  
        else:
            print("Invalid Vehicle Type") 

    def display_vehicle_details(self):
        print(self.__premium_amount)

v1 = Vehicle() 
v1.set__vehicle_type('Two Wheeler') 
v1.set_vehicle_cost(105000)
v1.calculate_premium()
v1.display_vehicle_details() 


v2 = Vehicle() 
v2.set__vehicle_type('Four Wheeler') 
v2.set_vehicle_cost(500000)
v2.calculate_premium()
v2.display_vehicle_details() 



class Instructor :
    def __init__(self) :
        self.__instructor_name = None
        self.__technology_skill = None        
        self.__experience = None
        self.__avg_feedback= None 

    def set_instructor_name(self , instructor_name):
        self.__instructor_name = instructor_name

    def get_instructor_name(self):
        return self.__instructor_name

    def set_technology_skill(self ,technology_skill):
        self.__technology_skill = technology_skill

    def get_technology_skill(self):
        return self.__technology_skill

    def set_experience(self , experience):
        self.__experience= experience

    def get_experience(self):
        return self.__experience

    def set_avg_feedback(self ,avg_feedback):
        self.__avg_feedback = avg_feedback

    def get_avg_feedback(self):
        return self.__avg_feedback

    def check_eligibility(self):
        if self.__experience > 3 and self.__avg_feedback>= 4.5:
            return True
        if self.__experience <= 3 and self.__avg_feedback>= 4:
            return True
        return False

    def allocate_course(self , technology):
        if self.check_eligibility():
            if technology in self.__technology_skill:
                return True
        return False

i1 = Instructor() 
i1.set_avg_feedback(4.5)
i1.set_experience(4)
i1.set_technology_skill(['JAVA','C++'])
print(i1.allocate_course('C++'))

''' 

courses={
    1001 : 25575.0,
    1002 : 15500.0
}

student_id_counter=1
class Student:

    def __init__(self) :
        self.__age=None
        self.__marks=None
        self.__student_id=None 
        self.__course_id = None
        self.__fees = None
    
    def validate_marks(self):
        if self.__marks>=0 and self.__marks<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age > 20:
            return True
        return False

    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            if self.__marks>= 65:
                print('Qualified')
                return True
        return False

    def set_age(self,age):
        self.__age=age 
    def get_age(self):
        return self.__age


    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks

    def set_fees(self,fees):
        self.__fees=fees
    def get_fees(self):
        return self.__fees

    def set_course_id(self,course_id):
        self.__course_id=course_id
    def get_course_id(self):
        return self.__course_id
        


    def set_student_id(self,student_id):
       
        self.__student_id=student_id
       
    def get_student_id(self):
        return self.__student_id

    def choose_course(self , course_id):
        if course_id in courses.keys():
            self.__course_id = course_id
            if self.__marks > 85 :
                self.__fees = courses[course_id]* 0.25
            else:
                self.__fees= courses[course_id] 
            return True
        else:
            return False


   
maddy=Student()
maddy.set_student_id(1004)
maddy.set_age(21)
maddy.set_marks(65)
if(maddy.check_qualification()):
    print("Student has qualified")
    if(maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")




class Classroom:
    classroom_list=[]

    @staticmethod
    def search_classroom(class_room):
        for room in Classroom.classroom_list:
            if class_room.lower() == room.lower():
                return 'Found' 
        return -1
        


