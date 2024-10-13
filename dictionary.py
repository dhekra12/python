# students ={
#     1:'dhekra',
#     2:'ahmed',
#     3:'ali',
#     4:'mohammed',
#     5:'taha',
#     }   
# # delet=students.clear()
# students={}
# students[6]='yusra'
# students[7]='boshra'
# students[8]='abdullah'
# students[4]='mahmoud'
# my_list =[]
# my_list.append('mona')


# # قاموس يحتوي على الأسماء و IDs
# students_data = {
#     1: "Alice",
#     2: "Bob",
#     3: "Charlie",
#     4: "Diana"
# }

# # تهيئة القاموس الفارغ
# students = {}

# # استخدام الدوارة لإضافة البيانات إلى القاموس وطباعة النتائج مع الفواصل
# print("The final dictionary of students:")
# for student_id, name in students_data.items():
#     students[student_id] = name
#     print(f"ID: {student_id}, Name: {name}")
#     print("-" * 20)  # طباعة خط فاصل بين العناصر
contacts ={}
name =input("what is your name? ").lower()
country =input("where are you from? ").lower() 
age =input("how old are you? ").lower() 
# contacts{name, country, age}
contacts["name"]=name
contacts["country"]=country
contacts['age']=age
print(contacts)







# book ={
#     "title": "Red Queen",
#     'author': 'Victoruia Averyard', 
#     'year' : 2015 ,
#     'pages' : 383,
#     'is_many' : True,
#     'rating' : 40.1,
#     'copies' : 2000
#     }
# print(book['pages'])