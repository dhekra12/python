import time

def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
    # return "@" in email and "." in email
    

def add_user(name, email):
    if validate_email(email):
        print(f"User '{name}' with email '{email}' successfully added.")
    else:
        print(f"Invalid Email format for user {name}, Registration failed")
user_name = input("Enter a user name: ")
user_email = input("Enter your email address: ")

print("checking user name .... please wait ")
time.sleep(2)
print("validating email address .... please wait ")
time.sleep(2)

# استدعاء الدالة
add_user(user_name, user_email)
