import random
print("Welcome to 'whose wallet'\n ")
print("you will gave me a list of names, and you will pick a person to pay")
persons_string = input("if you are ready, enter the separtated by a comma ").split(', ')
print(f"please sak {random.choice(persons_string)} to take his wallet out. dinner is on himز")

# هذه الطريقة تعلمك التفكير المنطقي واحتمال نحتاجها في برامج اخرى
# يفضل كتابة الكود بطريقة اكثر قابلية للقراءة على طريقة تقليل الأسطر
# 
# # names = persons_string.split(', ')
# length = len (names) - 1
# # for gave random person from list
# random_number = random.randint(0, length)
# random_person = names[random_number]
# print(f"please sak '{random_person}' to take his wallet out. dinner is on him ")
