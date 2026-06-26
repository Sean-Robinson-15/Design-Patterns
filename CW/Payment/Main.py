from Classes import *

def main():
    processor = Payment()
    amount = 106.00
    
    print("Credit Card")
    processor.set_strategy(CreditCardPayment("3141-5926-5358-9793", "044"))
    processor.process(amount)
    
    print("Crypto")
    processor.set_strategy(CryptoPayment("0xThisCryptoWalletAddress"))
    processor.process(amount)
    
    print("PayPal")
    processor.set_strategy(PayPalPayment("Lewis.Hamilton@Ferrari.com"))
    processor.process(amount)

if __name__ == "__main__":
    main()