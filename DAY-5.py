flowers = ['orchid','rose','jasmine']
levels = [15 , 25 , 40]

class Flower:
    def __init__(self) :
        self.__flower_name = None
        self.__price_per_kg=None
        self.__stock_available=None

    def validate_flower(self):
        if self.__flower_name.lower() in flowers:
            return True
        else:
            return False

    def validate_stock(self , required_quantity):
        if self.__stock_available >= required_quantity:
            return True
        else:
            return False
        
    def sell_flower(self , required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available -= required_quantity 

    def check_level(self):
        if self.validate_flower():
            flower_level = levels[flowers.index(self.__flower_name.lower())] #25
            if self.__stock_available<flower_level:
                return True
        return False 

    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name

    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg

    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available

    def get_stock_available(self):
        return self.__stock_available

    def get_price_per_kg(self):
        return self.__price_per_kg

    def get_flower_name(self):
        return self.__flower_name

a = Flower()
a.set_flower_name('Rose')
a.set_price_per_kg(200)
a.set_stock_available(26) 
print(a.check_level())




class CallDetail:
    def __init__(self, phoneno , called_no , duration ,call_type):
        self.__phoneno = phoneno 
        self.__called_no = called_no
        self.__duration = duration
        self.__call_type = call_type 


class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]            #[]
        for each_call in list_of_call_string:
            call_detail_list= each_call.split(",")
            a = CallDetail(call_detail_list[0],call_detail_list[1],call_detail_list[2],call_detail_list[3])
            self.list_of_call_objects.append(a) 

call='9990000001,9330000001,23,STD'  #[9990000001 , 9330000001 , 23 , STD ]
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)




class Bill:
    def __init__(self,bill_id,patient_name) :
        self.__bill_id= bill_id
        self.__patient_name = patient_name
        self.__bill_amount = 0 

    def get_bill_id(self):
        return self.__bill_id

    def get_patient_name(self):
        return self.__patient_name    

    def get_bill_amount(self):
        return self.__bill_amount 
    
    def calculate_bill_amount(self , consultation_fees, quantity_list, price_list):
        for i in range(len(quantity_list)):
            self.__bill_amount += (quantity_list[i] * price_list[i]) 
        self.__bill_amount += consultation_fees
        print(self.__bill_id)
        print(self.__patient_name)
        print(self.__bill_amount)

a = Bill(1 , 'NONE')
a.calculate_bill_amount(50 , [2 , 3 ] , [1,2])
a.get_bill_id()


class Parrot:
    __counter = 7000 
    def __init__(self,name , color):
        self.__name = name
        self.__color = color 
        self.__unique_number = Parrot.__counter + 1 

        Parrot.__counter= Parrot.__counter+1

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_unique_number(self):
        return self.__unique_number




class Customer:
    def __init__(self,phone_no,name,age):
        self.phone_no=phone_no
        self.name=name
        self.age=age
        self.list_of_calls=None

class CallDetail:
    def __init__(self,phone_no,called_no,duration):
        self.phone_no=phone_no
        self.called_no=called_no
        self.duration=duration

class Util:
    def __init__(self):
        self.list_of_customer_calldetail_objects = None
    def parse_customer(self,list_of_customers,list_of_calls):
        self.list_of_customer_calldetail_objects = []
        for customer in list_of_customers:
            customer.list_of_calls=[]    #[]
            for call in list_of_calls:
                if customer.phone_no == call.phone_no:
                     customer.list_of_calls.append(call) # cust1 = [call1 , call4 , call5] cust2=[call3] cus3=[call2 , 6 , 7]
            self.list_of_customer_calldetail_objects.append(customer)
            #[[call1 , call4 , call5] ,[call3] , [call2 , 6 , 7] ]


cust1=Customer(9900009901,'cust1',23)
cust2=Customer(9900009902,'cust2',24)
cust3=Customer(9900009903,'cust3',25)
list_of_customers=[cust1,cust2,cust3]

call1=CallDetail(9900009901,8800123401,5)
call2=CallDetail(9900009903,8800123402,10)
call3=CallDetail(9900009902,8800123403,2)
call4=CallDetail(9900009901,8800123404,8)
call5=CallDetail(9900009901,8800123405,7)
call6=CallDetail(9900009903,8800123406,9)
call7=CallDetail(9900009903,8800123407,4)
list_of_calls=[call1,call2,call3,call4,call5,call6,call7]

Util().parse_customer(list_of_customers, list_of_calls)



class Customer:
    def __init__(self, customer_name ,customer_id , address) :
        self.__customer_id = customer_id            
        self.__customer_name = customer_name                
        self.__address = address           

    def validate_customer_id(self):
        id = str(self.__customer_id)     
        if id[0]=='1' and len(id)==6 :
            return True
        else:
            return False

    def get_customer_id(self):
        return self.__customer_id
    def get_customer_name(self):
        return self.__customer_name
    def get_address(self):
        return self.__address
   
class Freight:
    counter = 198 
    def __init__(self,recipient_customer,from_customer , weight , distance):
        self.__weight = weight
        self.__distance = distance
        self.__from_customer = from_customer
        self.__recipient_customer = recipient_customer
        self.__freight_id=0
        self.__freight_charge = 0

    def validate_weight(self):
        if self.__weight%5 == 0 :
            return True
        else:
            return False
    
    def validate_distance(self):
        if 500<= self.__distance<=5000:
            return True
        else:
            return False
        
    def forward_cargo(self):
        if Customer.validate_customer_id(self.__from_customer) and Customer.validate_customer_id(self.__recipient_customer) and self.validate_distance() and self.validate_weight():
            self.__freight_id = Freight.counter+2 

            Freight.counter += 2 
            self.__freight_charge= (self.__weight*150)+(self.__distance*60)
        else:
            self.__freight_charge=0

    def get_freight_charge(self):
        return self.__freight_charge
    def get_freight_id(self):
        return self.__freight_id
    def get_receipient_customer(self):
        return self.__receipient_customer
    def get_from_customer (self):
        return self.__from_customer 
    def get_distance (self):
        return self.__distance 
    def get_weight(self):
        return self.__weight 

c1= Customer(112233,'Jack','London')
c2= Customer(112334,'Jill','Hill')
f1 = Freight(c1 ,c2, 5 , 500)
f1.forward_cargo()
print(f1.get_freight_charge())




class Item:
    def __init__(self,item_id ,description , price_per_quantity):
        self.__item_id = item_id
        self.__description = description
        self.__price_per_quantity = price_per_quantity

    def get_item_id(self):
        return self.__item_id
    def get_description(self):
        return self.__description
    def get_price_per_quantity(self):
        return self.__price_per_quantity




class Bill:
    counter = 1000
    def __init__(self) :
        self.__bill_id = 1000
        self.__bill_amount =0 

    def generate_bill_amount(self , item_quantity,items):
        Bill.counter+=1 
        self.__bill_amount=0
        self.__bill_id='B'+str(Bill.counter) 
        tmp_dict = item_quantity
        a = {}
        for item in tmp_dict:
            a[item.lower()] = tmp_dict[item]
        for product , quantity in a.items():
            for item in items:
                if item.get_item_id().lower() == product:
                    self.__bill_amount+=quantity*item.get_price_per_quantity()
                    break

    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount


class Customer:
    def __init__(self,customer_name) :
        self.__customer_name = customer_name
        self.__payment_status = None
    
    def pays_bill(self , bill):
        self.__payment_status='Paid'

        print(self.__customer_name)

        print(bill.get_bill_id())
        print(bill.get_bill_amount())

    def get_customer_name(self):
        return self.__customer_name()
    def get_customer_name(self):
        return self.__payment_status


item_quantity={'aaa':3 , 'bbb':2 , 'ccc':4 , 'ddd':2}
c = Customer("Sneha") 
i1=Item('aaa','maggie',12.00)
i2=Item('bbb','pasta',120.00)
i3=Item('ccc','chocolate',112.00)
i4=Item('aaa','noodles',128.00)
i5=Item('aaa','fruits',120.00)
i6=Item('aaa','vegetables',120.00) 

items=[i1,i2,i3,i4,i5,i6]
b=Bill()
b.generate_bill_amount(item_quantity,items)
c.pays_bill(b) 


destination_list=['Mumbai', 'Chennai', 'Pune' , 'Kolkata']

class Ticket :
    counter = 0

    def __init__(self , passenger_name,source,destination):
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        self.__ticket_id=None    

    def validate_source_destination(self): 
        if self.__source.title()=='Delhi':
            if self.__destination.title() in destination_list:
                return True
        return False

    def generate_ticket(self):
        Ticket.counter +=1 
        if self.validate_source_destination():
            if Ticket.counter<10:
                self.__ticket_id=self.__source[0]+self.__destination[0]+'0'+str(Ticket.counter)
            else:
                self.__ticket_id=self.__source[0]+self.__destination[0]+str(Ticket.counter)

    def get_passenger_name(self):
        return self.__passenger_name
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination
    def get_ticket_id(self):
        return self.__ticket_id


#lex_auth_012751886858420224260
class Patient:
    def __init__(self,patient_id,patient_name,list_of_lab_test_ids):
        self.__patient_id=patient_id
        self.__patient_name=patient_name
        self.__list_of_lab_test_ids=list_of_lab_test_ids
        self.__lab_test_charge=0
    def get_patient_id(self):
        return self.__patient_id
    def get_patient_name(self):
        return self.__patient_name
    def get_list_of_lab_test_ids(self):
        return self.__list_of_lab_test_ids
    def get_lab_test_charge(self):
        return self.__lab_test_charge
    def calculate_lab_test_charge(self):
        for test in self.__list_of_lab_test_ids:
            if LabTestRepository.get_test_charge(test)>0:
                self.__lab_test_charge += LabTestRepository.get_test_charge(test)

	    #Remove pass and write the logic here.

class LabTestRepository:
    __list_of_hospital_lab_test_ids=["L101","L102","L103","L104"]
    __list_of_lab_test_charge=[2020,1750.50,5700,1320.50]
    @staticmethod
    def get_test_charge(lab_test_id):
        if lab_test_id in LabTestRepository.__list_of_hospital_lab_test_ids:
            I1= LabTestRepository.__list_of_hospital_lab_test_ids.index(lab_test_id)
            return LabTestRepository.__list_of_lab_test_charge[I1]
        else:
            return -1  

	    #Remove pass and write the logic here.

lab_test_list1=["L101","L103","L104",'L105']
patient1=Patient(1234,"Sam",lab_test_list1)
patient1.calculate_lab_test_charge()
print("Patient id:",patient1.get_patient_id(),"\nPatient name:",patient1.get_patient_name(),"\nPatient's test ids:",patient1.get_list_of_lab_test_ids(), "\nTotal lab test charge:",patient1.get_lab_test_charge())














