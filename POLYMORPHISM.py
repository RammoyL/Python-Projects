

#Parent Class User
class User:
    name = 'Terry'
    email = 'mynameisTerry@gamil.com'
    password = 'Dgr38r72'

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email you entered is incorrect.")

#Child Class Employee
class Employee(User):
    nase_pay = 11.00
    department = 'General'
    pin_number = '3980'

# This is the same method in the parent class "User".
# The difference is that, isntead of using entry_passwordm we're using entry_pin.

   def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_mumber):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email you entered is incorrect.")

#The following code invokes the methods inside each class for User and Employee.

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
