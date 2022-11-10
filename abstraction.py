

from abc import ABC, abstractmethod
class home(ABC):
    def rent(self, amount):
        print("Total amount due: ",amount)
#this function wants us to pass in an argument, but we won't indicate how or what kind of data
    @abstractmethod
    def payment(self, amount):
        pass

class debitPayment(home):
#here is the payment function is defined and implimented from its parent class "rent".
    def payment(self,amount):
        print("Your recent payment of {} exceeds the limit of your current balance of $900 ".format(amount))

obj = debitPayment()
obj.rent("$985")
obj.payment("$1,012")
