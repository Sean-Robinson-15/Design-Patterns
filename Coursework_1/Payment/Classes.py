from abc import ABC, abstractmethod

#Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
#Credit Card Strategy
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, amount):
        print(f"Credit Card payment of £{amount:.2f} made from {self.card_number}")
        
#Crypto Strategy        
class CryptoPayment(PaymentStrategy):
    def __init__(self, wallet):
        self.wallet = wallet
        
    def pay(self, amount):
        print(f"Crypto payment of £{amount:.2f} made from {self.wallet}")
        
#PayPal Strategy
class PayPalPayment(PaymentStrategy):
    def __init__(self, account):
        self.account = account
        
    def pay(self, amount):
        print(f"PayPal payment of £{amount:.2f} made from {self.account}")
        
#Context Class        
class Payment:
    def __init__(self):
        self._strategy = None
        
    def set_strategy(self, strategy):
        self._strategy = strategy
        
    def process(self, amount):
        if not self._strategy:
            print("Please select a payment method")
            return
        if amount <= 0 or not isinstance(amount, float):
            print("Paymont amount is incorrect")
            return
        self._strategy.pay(amount)