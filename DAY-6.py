class Multiplex:
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=[None,None]
    __list_ticket_price=[150,200]
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    def get_total_price(self):
        return self.__total_price
    def get_seat_numbers(self):
        return self.__seat_numbers



    def book_ticket(self, movie_name, number_of_tickets):
        if movie_name.lower() not in Multiplex.__list_movie_name:
            return 0                       #  0 
        elif Multiplex.__list_total_tickets[Multiplex.__list_movie_name.index(movie_name)] < number_of_tickets:
            return -1 
        else:
            i1 = Multiplex.__list_movie_name.index(movie_name)
            self.__seat_numbers=self.generate_seat_number(i1,number_of_tickets)
            self.calculate_ticket_price(i1,number_of_tickets) 

    def  generate_seat_number(self,movie_index, number_of_tickets):
        tkt_list =[]
        if movie_index == 0:
            if Multiplex.__list_last_seat_number[0] is None:
                lst_tkt = 0 
            
            else:
                lst_tkt = int(Multiplex.__list_last_seat_number[0].split('-')[-1])  # M1-1 [M1 , 1 ]
            prefix = 'M1'

            for i in range (lst_tkt+1 , lst_tkt+number_of_tickets+1):  #(2 , 5)   2 , 3 , 4
                tkt_list.append(prefix+'-'+str(i)) #[M1-2 , M1-3 , M1-4 ] 
            Multiplex.__list_last_seat_number[0] = tkt_list[-1] 
            Multiplex.__list_total_tickets[0] -= number_of_tickets

        else:
            if movie_index == 1:
                if Multiplex.__list_last_seat_number[1] is None:
                    lst_tkt = 0 

                else:
                    lst_tkt = int(Multiplex.__list_last_seat_number[1].split('-')[-1])  # M1-1 [M1 , 1 ]
                prefix = 'M1'

                for i in range (lst_tkt+1 , lst_tkt+number_of_tickets+1):  #(2 , 5)   2 , 3 , 4
                    tkt_list.append(prefix+'-'+str(i)) #[M1-2 , M1-3 , M1-4 ] 
                Multiplex.__list_last_seat_number[1] = tkt_list[-1] 
                Multiplex.__list_total_tickets[1] -= number_of_tickets

        return tkt_list

booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status=booking2.book_ticket("movie2",6)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price()) 









class Apparel:
    counter = 100 
    def __init__(self,price , item_type) :
        self.__price = price
        self.__item_type = item_type
        self.__item_id = None
        if self.__item_type=='Cotton':
            Apparel.counter+=1 
            self.__item_id= 'C'+str(Apparel.counter)
        elif self.__item_type=='Silk':
            Apparel.counter+=1 
            self.__item_id= 'S'+str(Apparel.counter) 

    def calculate_price(self):
        self.__price=self.__price + self.__price*0.05 
    
    def get_price(self):
        return self.__price
    
    def get_item_type(self):
        return self.__item_type   
    
    def set_price(self,price):
        self.__price=price
    
class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(price, 'Cotton')
        self.__discount=discount


    def calculate_price(self):
        super().calculate_price()
        price = self.get_price()
        price = price - (price*(self.__discount/100)) 
        price = price + price*0.05 
        Apparel.set_price(self,price)

    def get_discount(self):
        return self.__discount 


class Silk(Apparel):
    def __init__(self, price):
        super().__init__(price, 'Silk')
        self.__points = 0 

    def calculate_price(self):
        super().calculate_price()
        price = self.get_price() 
        if price>10000:
            self.__points = 10 
        else:
            self.__points=3 

        price = price + price*0.10
        Apparel.set_price(self,price) 

    def get_points(self):
        return self.__points




class FruitInfo:
    __fruit_name_list=['Apple','Guava','Orange','Grape','Sweet Lime']
    __fruit_price_list=[200,80,70,110,60] 

    @staticmethod
    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.__fruit_name_list:
            fruit_index = FruitInfo.__fruit_name_list.index(fruit_name)
            price_per_kg =FruitInfo.__fruit_price_list[fruit_index]
            return price_per_kg 

        else:
            return -1 

    @staticmethod
    def get_fruit_name_list():
        return FruitInfo.__fruit_name_list 

    @staticmethod
    def get_fruit_price_list():
        return FruitInfo.__fruit_price_list

class Purchase:
    __counter = 101 
    def __init__(self,customer , fruit_name, quantity):
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity
        self.__purchase_id = None 

    def calculate_price(self):
        price = FruitInfo.get_fruit_price(self.__fruit_name)
        if FruitInfo.get_fruit_price(self.__fruit_name) != -1:
            mx = FruitInfo.get_fruit_price_list()
            maximum = max(mx) 
            minimum = min(mx) 
            total_price = price* self.__quantity 

            if price==maximum and self.__quantity>1:
                total_price = total_price * 0.98     #(total_price=total_price-total_price*0.02)

            if price== minimum and self.__quantity>=5: 
                total_price = total_price * 0.95 

            if Customer.get_cust_type(self.__customer)  == 'wholesale':
                total_price = total_price * 0.90

            self.__purchase_id='P'+ str(Purchase.__counter) 
            Purchase.__counter+=1

            return total_price
        else:
            return -1 

    def get_customer(self):
        return self.__customer
    def get_fruit_name(self):
        return self.__fruit_name
    def get_quantity(self):
        return self.__quantity
    def get_purchase_id(self):
        return self.__purchase_id


class Customer:
    def __init__(self, customer_name, cust_type):
        self.__customer_name = customer_name
        self.__cust_type = cust_type

    def get_customer_name(self):
        return self.__customer_name
    def get_cust_type(self):
        return self.__cust_type



c = Customer('Tom','wholesale') 
p = Purchase(c ,'Guava',2)
print(p.calculate_price())



class ThemePark:
    #dict_of_games contains the game name as key, price/ride and points that can be earned by customer in a list as value
    dict_of_games={"Game1":[35.5,5], "Game2":[40.0,6],"Game3":[120.0,10], "Game4":[60.0,7],"Game5":[25.0,4]}
    @staticmethod
    def validate_game(game_input):
        game = ThemePark.dict_of_games.keys()#["Game1","Game2"]
        if game_input in game:
            return True
        else:
            return False 
        #Remove pass and write the logic here
        #If game_input is present in ThemePark, return true. Else, return false.
    @staticmethod
    def get_points(game_input):
        for key , value in ThemePark.dict_of_games.items():
            if game_input==key:
                return value[1]
        #Remove pass and write the logic here
        #Return the points that can be earned for the given game_input.
    @staticmethod
    def get_amount(game_input):
        for key , value in ThemePark.dict_of_games.items():
            if game_input==key:
                return value[0]
        #Remove pass and write the logic here
        #Return the price/ride for the given game_input

#This class represents ticket
class Ticket:
    __ticket_count=200
    def __init__(self):
        self.__ticket_id=None
        self.__ticket_amount=0
    def generate_ticket_id(self):
        Ticket.__ticket_count +=1
        self.__ticket_id = Ticket.__ticket_count 
        #Remove pass and write the logic here
        #Auto-generate ticket_id starting from 201
    def calculate_amount(self, list_of_games):
        for game in list_of_games:           #[game1 , game2 ]
            if ThemePark.validate_game(game):
                self.__ticket_amount += ThemePark.get_amount(game)  # ta = 35.5 + 40.0 = 75.5 
            else:
                self.__ticket_amount=0
                return False
        return True

        #Remove pass and write the logic here
        #Validate the games in the list_of_games.
       # If all games are valid, calculate total ticket amount and assign it to attribute, ticket_amount and return true. Else, return false
    def get_ticket_id(self):
        return self.__ticket_id
    def get_ticket_amount(self):
        return self.__ticket_amount

class Customer:
    def __init__(self,name , list_of_games) :
        self.__name = name
        self.__list_of_games = list_of_games
        self.__ticket = Ticket()
        self.__points_earned = 0
        self.__food_coupon = 'No'

    def play_game(self):
        if 'Game3' in self.__list_of_games:
            self.__list_of_games.append("Game2")
        for i in self.__list_of_games:
            point = ThemePark.get_points(i)
            self.__points_earned += point 

    def update_food_coupon(self):
        if 'Game4' in self.__list_of_games and self.__points_earned>15:
            self.__food_coupon='Yes' 

    def book_ticket(self):
        if Ticket.calculate_amount(self.__ticket,self.__list_of_games):
            Ticket.generate_ticket_id(self.__ticket) 
            self.play_game()
            self.update_food_coupon()
            return True
        else:
            return False
    def get_name(self):
        return self.__name
    def get_list_of_games(self):
        return self.__list_of_games
    def get_ticket(self):
        return self.__ticket
    def get_points_earned (self):
        return self.__points_earned 
    def get_food_coupon (self):
        return self.__food_coupon 

    #Remove pass and implement class Customer here
 
class Company:
    #Stores hike% based on job level.
    dict_hike={"A":5, "B":6, "C":10 , "D":11}
    #Consider incentive provided in all classes to be in Rupees(Rs).
    __c_incentive=5000
    def __init__(self,name):
        self.name=name
    @staticmethod
    def get_c_incentive():
        return Company.__c_incentive
class Employee:
    def __init__(self, emp_id,e_incentive, job_level,salary, performance_list):
        self.emp_id=emp_id
        self.__e_incentive=e_incentive
        self.__salary=salary
        self.__job_level=job_level
        self.__performance_list=performance_list
    def get_e_incentive(self):
        return self.__e_incentive
    def get_performance_list(self):
        return self.__performance_list
    def get_salary(self):
        return self.__salary
    def get_job_level(self):
        return self.__job_level
    def identify_performance_hike(self):
        return None
    def identify_job_level_hike(self):
        return None
    def identify_incentive(self):
        return None
    def update_salary(self,hike, incentive):
        self.__salary= (self.__salary+ self.__salary*hike/100) + incentive
    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                hike+=ex_hike
            incentive=self.identify_incentive()
            self.update_salary(hike, incentive)
            return True
        else:
            return False

class PermanentEmployee(Employee):
    def __init__(self, emp_id, e_incentive, job_level, salary, performance_list,p_incentive):
        super().__init__(emp_id, e_incentive, job_level, salary, performance_list)
        self.__p_incentive = p_incentive

    def get_p_incentive(self):
        return self.__p_incentive
    
    def identify_performance_hike(self):
        performance_list = self.get_performance_list()
        if performance_list[4]==1 and performance_list[3]==1:
            hike = 5
        elif performance_list[4]==1 and performance_list[3]==2 and  performance_list[2]==1:
            hike = 3
        else:
            hike=None
        return hike

    def identify_job_level_hike(self):
        job_level = Employee.get_job_level(self)
        if job_level in Company.dict_hike.keys():
            job_hike = Company.dict_hike[job_level] 
            return job_hike
        else:
            return None

    def identify_incentive(self):
        c_incentive = Company.get_c_incentive() 
        e_incentive = Employee.get_e_incentive(self)
        incentive = c_incentive+e_incentive+self.__p_incentive
        return incentive

    def calculate_salary(self):
        jl_hike=self.identify_job_level_hike()
        ex_hike=self.identify_performance_hike()
        if(jl_hike!=None):
            hike=jl_hike
            if(ex_hike!=None):
                hike+=ex_hike
            incentive=self.identify_incentive()
            Employee.update_salary(self,hike,incentive)
            return True
        else:
            return False


pizza =['small','medium']
class Customer :
    def __init__(self,customer_name , quantity) :
        self.__customer_name = customer_name
        self.__quantity = quantity

    def validate_quantity(self):
        if self.__quantity in range(1 , 6):
            return True
        else:
            return False

    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity

class Pizzaservice:
    counter = 100 

    def __init__(self,customer,pizza_type ,additional_topping) :
        self.__customer = customer
        self.__pizza_type  = pizza_type 
        self.__additional_topping = additional_topping
        self.__service_id = None
        self.pizza_cost = 0

    def get_customer(self):
        return self.__customer
    def get_pizza_type(self):
        return self.__pizza_type
    def get_additional_topping (self):
        return self.__additional_topping 
    def get_service_id(self):
        return self.__service_id
    def get_pizza_cost(self):
        return self.__pizza_cost

    def validate_pizza_type(self):
        if self.__pizza_type.lower() in pizza:
            return True
        else:
            return False


    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer.validate_quantity(self.__customer):
            if self.__pizza_type.lower()=='small' and self.__additional_topping==True:
                self.pizza_cost= (150 + 35 )*Customer.get_quantity(self.__customer)
            if self.__pizza_type.lower()=='small' and self.__additional_topping==False:
                self.pizza_cost= (150 )*Customer.get_quantity(self.__customer)
            if self.__pizza_type.lower()=='medium' and self.__additional_topping==True:
                self.pizza_cost= (200 + 50 )*Customer.get_quantity(self.__customer)
            if self.__pizza_type.lower()=='medium' and self.__additional_topping==False:
                self.pizza_cost= (200)*Customer.get_quantity(self.__customer)

            self.__service_id= self.__pizza_type[0]+str(Pizzaservice.counter+1)
            Pizzaservice.counter+=1 
        else:
            self.pizza_cost= -1

    
class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping,distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__distance_in_kms = distance_in_kms
        self.__delivery_charge = 0 

    def get_distance_in_km(self):
        return self.__distance_in_kms
    def get_delivery_charge(self):
        return self.__delivery_charge

    def validate_distance_in_kms(self):
        if 1 <= self.__distance_in_kms<=10:
            return True
        return False

    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms() == True :
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost !=-1 :
                if self.__distance_in_kms < 6 :
                    self.__delivery_charge= self.__distance_in_kms*5 
                else:
                    distance = self.__distance_in_kms-5 
                    self.__delivery_charge = 25 + (distance*7) 
                self.pizza_cost += self.__delivery_charge
            else:
                self.pizza_cost=-1


c = Customer('Asha',5) 
p = Pizzaservice(c,'medium',False) 
d = Doordelivery(c , 'medium',False,8) 

d.calculate_pizza_cost()
print(d.pizza_cost)
