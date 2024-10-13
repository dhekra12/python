import time
def calculate_tax(income):
    return income * 0.15

def calculate_total_salary(base_salary, bonus):
    total_salary= base_salary + bonus
    tax_to_pay= calculate_tax(total_salary)
    return total_salary- tax_to_pay

base_salary= float(input("Enter your base salary: "))
bonus= float(input("How much bonus did you get: "))

final_salary= calculate_total_salary(base_salary , bonus)

time.sleep(3)
print("Calculating your total salary ..... please wait")
time.sleep(2)
print("Finding the tax amount in Yemen ..... please wait")
time.sleep(2)
print("calculating your final salary ..... please wait")
time.sleep(2)
print(f"final salary after tax: ${final_salary}")
