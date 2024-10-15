import os
import time

dollar= """
   ||====================================================================||
   ||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
   ||(100)==================| DHEKRA MOHAMMED |================(100)||
   ||\\$//        ~         '------========--------'                \\$//||
   ||<< /        /$\              // ____ \\                         \ >>||
   ||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
   ||<<|        \\ //           || <||  >\  ||                        |>>||
   ||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||====================================================================||>||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||<||
||(100)==================| DHEKRA MOHAMMED |================(100)||>||
||\\$//        ~         '------========--------'                \\$//||\||
||<< /        /$\              // ____ \\                         \ >>||)||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||/||
||<<|        \\ //           || <||  >\  ||                        |>>||=||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||"""

def clear_terminal():
   

    os.system('cls' if os.name == 'nt' else 'clear')

exchange_rates= {
   "": dollar,
   "USD": 1.0,
   "EUR": 0.85,
   "EGP": 30.9,
   "RMB": 6.5,
}
def display_rates():
   print('Welcome to "Currency coverter" ')
   for currency in exchange_rates:
      print(f"{currency}: {exchange_rates[currency]}")

def currency_convert():
   clear_terminal()
   display_rates()
   
   
   

from_currency=input("\nchoose a currency to convert from: ").upper()
while True:
   amount=float(input("Enter the amount: "))

   confirmation=input(f"\nyou enter {amount} {from_currency}. Confirm? (Y/N) : ").upper()

   if confirmation == "Y":
      break
clear_terminal()
display_rates()

to_currency=input("\nchoose a currency to convert to: ").upper()

print("Analyzing your your request  .... please wait ")
time.sleep(2)
print(f"checking for {to_currency} best rates available .... please wait ")
time.sleep(3)
print(f"getting a discount price for {from_currency} .... please wait ")
time.sleep(2)
if from_currency not in exchange_rates or to_currency not in exchange_rates:
   print("Invalid currency. Conversion canceld.")
   time.sleep(2)
   # إيجاد معدل التحويل
new_rate= exchange_rates[to_currency]/exchange_rates[from_currency]

# حول العملة عن طريق معدل التحويل
converted_amount= amount * new_rate
clear_terminal()

print(
   f"preparing the dealfrom {from_currency} to {to_currency}.... please wait\n"
)
time.sleep(2)
print(
   f"Exchange Rate: 1 {from_currency} = {new_rate} {to_currency}.... please wait\n"
)
time.sleep(2)

print(
   f" {amount} = {from_currency} is equal to {round[converted_amount,2]} {to_currency}"
)
time.sleep(1)

accept_transaction=input(
   f"\nDo you accept this transaction? (Y/N): ").upper()

if accept_transaction =="Y":
   print("Transaction Successful!")
else:
   print("Transaction Canceled.")
   
another_conversion=input(
   f"\nDo you want to perform another conversion? (Y/N): ").upper()

if another_conversion =="Y":
   currency_convert()
else:
   print("Thanks for using the currency converter!")
   
# start the currancy converter
currency_convert() 
   
