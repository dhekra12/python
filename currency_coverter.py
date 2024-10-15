import os
import time

# ورقة الدولار
dollar = """
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

# معدلات الصرف
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "EGP": 30.9,
    "RMB": 6.5,
}

def display_rates():
    print('Welcome to "Currency converter" ')
    for currency, rate in exchange_rates.items():
        print(f"{currency}: {rate}")

def currency_convert():
    while True:
        clear_terminal()
        display_rates()
        
        # اختيار العملة
        from_currency = input("\nChoose a currency to convert from (USD, EUR, EGP, RMB): ").upper()
        if from_currency not in exchange_rates:
            print("Invalid currency. Please try again.")
            continue

        # إدخال المبلغ
        amount = float(input("Enter the amount: "))
        
        # تأكيد المبلغ
        confirmation = input(f"\nYou entered {amount} {from_currency}. Confirm? (Y/N): ").upper()
        if confirmation != "Y":
            continue

        clear_terminal()
        display_rates()

        # اختيار العملة المستهدفة
        to_currency = input("\nChoose a currency to convert to (USD, EUR, EGP, RMB): ").upper()
        if to_currency not in exchange_rates:
            print("Invalid currency. Please try again.")
            continue
        
        # عمليات التحويل الوهمية
        print("Analyzing your request... please wait ")
        time.sleep(2)
        print(f"Checking for {to_currency} best rates available... please wait ")
        time.sleep(2)
        print(f"Getting a discount price for {from_currency}... please wait ")
        time.sleep(2)

        # إيجاد معدل التحويل
        new_rate = exchange_rates[to_currency] / exchange_rates[from_currency]

        # حول العملة عن طريق معدل التحويل
        converted_amount = amount * new_rate
        clear_terminal()

        # عرض المعلومات
        print(f"Preparing the deal from {from_currency} to {to_currency}... please wait\n")
        time.sleep(2)
        print(f"Exchange Rate: 1 {from_currency} = {new_rate} {to_currency}\n")
        time.sleep(2)

        # عرض المبلغ المحول
        print(f"{amount} {from_currency} is equal to {round(converted_amount, 2)} {to_currency}")

        # تأكيد قبول الصفقة
        accept_transaction = input(f"\nDo you accept this transaction? (Y/N): ").upper()
        if accept_transaction == "Y":
            print("Transaction Successful!")
        else:
            print("Transaction Canceled.")

        # السؤال عن تحويل آخر
        another_conversion = input(f"\nDo you want to perform another conversion? (Y/N): ").upper()
        if another_conversion != "Y":
            print("Thanks for using the currency converter!")
            break

# البدء ببرنامج التحويل
currency_convert()
