Saul
Resendiz

   	MODULE 11 LAB


   QUESTION #1):

# CREATING EMPLOYEE CLASS
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
   
    def set_name(self, name):
        self.__name = name
            
    def set_number(self, number):
        self.__number = number
        
    def get_name(self):
        return self.__name
            
    def get_number(self):
        return self.__number
        
# PRODUCTION WORKER CLASS:
class ProductionWorker(Employee):
    def __init__(self, name, number, shift, hourly_pay):
        super().__init__(name, number)
        self.__shift = shift
        self.__hourly_pay = hourly_pay

    # Getter methods
    def get_shift(self):
        return self.__shift
    
    def get_hourly_pay(self):
        return self.__hourly_pay
    
    # Setter methods
    def set_shift(self, shift):
        self.__shift = shift
    
    def set_hourly_pay(self, hourly_pay):
        self.__hourly_pay = hourly_pay

# MAIN FUNCTION:
def main():
    # Creating production worker object and receiving input 
    name = input("Enter the employee's name: ")
    number = input("Enter the employee's number: ")
    shift = int(input("Enter the type of shift (Enter 1 for day shift, 2 for night shift): "))
    hourly_pay = float(input("Enter the hourly pay rate: $"))

    worker_object = ProductionWorker(name, number, shift, hourly_pay)

    # Display the information using accessor methods
    print("\nWORKER FULL INFORMATION:")
    print(f"Name: {worker_object.get_name()}")
    print(f"Worker's Number: {worker_object.get_number()}")
    print(f"Worker Shift: {worker_object.get_shift()}")
    print(f"Hourly Pay Rate: ${worker_object.get_hourly_pay()}")

if __name__ == "__main__":
    main()


	QUESTION #2):

# CREATING SHIFT SUPERVISOR CLASS:

class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, production_bonus):
        Employee.__init__(self, name, number)
        self.annual_salary = annual_salary
        self.production_bonus = production_bonus
      
     #SETTER METHODS 
    def set_annual_salary(self, annual_salary):
        self.annual_salary = annual_salary
    
    def set_production_bonus(self, production_bonus):
        self.production_bonus = production_bonus

    # GETTER METHODS
    def get_annual_salary(self):
        return self.annual_salary
    
    def get_production_bonus(self):
        return self.production_bonus
  
# MAIN 
def main():
    # CREATING SHIFT SUPERVISOR OBJECT
    name = input("Enter shift supervisor's name: ")
    number = input("Enter their employee number: ")
    annual_salary = float(input("Enter their annual salary: $"))
    production_bonus = float(input("Enter their production bonus: $"))

    supervisor_object = ShiftSupervisor(name, number, annual_salary, production_bonus)

    # DISPLAY SHIFT SUPERVISOR:
    print("\n Shift Supervisor Info: ")
    print ('-----------------------------------')
    print(f" Supervisor's Name: {supervisor_object.get_name()}")
    print(f"Supervisor's Number: {supervisor_object.get_number()}")
    print(f"Annual Salary: ${supervisor_object.get_annual_salary()}")
    print(f"Production Bonus: ${supervisor_object.get_production_bonus()}")

if __name__ == "__main__":
    main() 


	QUESTION #3):

# CREATING PERSON CLASS  

class Person:
    # Intializing object
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
        
    # SETTER METHODS
    def set_name(self, name):
        self.__name = name
        
    def set_address(self, address):
        self.__address = address
        
    def set_phone(self, phone):
        self.__phone = phone
        
    # GETTER METHODS    
    def get_name(self):
        return self.__name
        
    def get_address(self):
        return self.__address
        
    def get_phone(self):
        return self.__phone
        
# CREATING CUSTOMER CLASS 
class Customer(Person):
    def __init__(self, name, address, phone, customer_number, mailing_list):
        Person.__init__(self, name, address, phone)
        
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list
        
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number
        
    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list
        
    def get_customer_number(self):
        return self.__customer_number
        
    def get_mailing_list(self):
        return self.__mailing_list
        
# CREATING CUSTOMER OBJECT
name = input('Name: ')
address = input('Address: ')
phone = input('Phone Number: ')
customer_number = input('Customer Number: ')
mail = input('Include in mailing list? (y/n): ')

if (mail.lower() == 'y'):
    mailing_list = True
else :
    mailing_list = False
    
my_customer = Customer(name, address, phone, customer_number, mailing_list)

# PRINTING CUSTOMER INFO TO CONSOLE
print('\nCustomer Info:')
print('--------------------------')
print('Name:', my_customer.get_name())
print('Address:', my_customer.get_address())
print('Phone:', my_customer.get_phone())
print('Customer Number:', my_customer.get_customer_number())
print('Mailing List:', my_customer.get_mailing_list())
