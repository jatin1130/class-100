class Atm (object) :
    def __init__(self,cardNumber,pinNumber,cashNeeded,totalAmount):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.cashNeeded = cashNeeded
        self.totalAmount = totalAmount

    def tranasaction(self) :
        print("card number : " , self.cardNumber)
        print("your pin : " , self.pinNumber)
        print("withdrawl : " , self.cashNeeded)

    def balance(self) :
        print("your balance = ",self.totalAmount - self.cashNeeded)

person1 = Atm(5468923455,"****",2500,1000000)
person2 = Atm(7649186151,"****",5000,650000)

person1.tranasaction()
person1.balance()

person2.tranasaction()
person2.balance()