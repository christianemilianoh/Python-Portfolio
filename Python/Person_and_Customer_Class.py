#Establishing the main method which will contain all the code for classes, mutators, accessors and attributes.
def main():
    #Initialize the person class, which will contain attributes for people.
    class Person:
        #This defenition initalizes the name, address and phone number for the person.
        def __init__(self, name, address, tele_num):
            self.name = name
            self.address = address
            self.tele_num = tele_num

    #The customer sublass calls attributes from person. It uses super() to inherit from the Person class.
    class Customer(Person):
        #Initilaztion definition of the standard attributes alongside the customer number, and if the customer is on the mailing list.
        def __init__(self, name, address, tele_num, customer_num, mail_list):
            #The super() initilzation inherits person data while adding customer number and the boolean maling list attribute.
            super().__init__(name, address, tele_num)
            self.customer_num = customer_num
            self.mail_list = mail_list

    #A customers data, containing name, address, phone number, customer case number and the boolean result if they're on a mailing list using those parameters.
    customer = Customer("Walter White", "308 Negra Arroyo Lane", "123-1234-1234", 7, True)
    
    #These print statements are pulling from the accessors from the Person and Customer class, and output them on a seperate line with a title and colon preceeding the value.
    print(f"Name: {customer.name}")
    print(f"Address: {customer.address}")
    print(f"Telephone Number: {customer.tele_num}")
    print(f"Customer Number: {customer.customer_num}")
    print(f"Mailing List: {customer.mail_list}")

#Calling the main function in order to run the whole program.
main()