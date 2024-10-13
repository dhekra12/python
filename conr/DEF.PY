def take_order(name):
    # name=input("What is your name? ")
    print(f"Welcome to the resturant, {name} ")
    print("Order taken successfully.  ")
    thank_customer(name)
    
def thank_customer(name):
        print(f"Thank you,{name} for choosing our resturant! ")
    
        
take_order(input("What is your name? "))
