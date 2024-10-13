import string

# # تعريف الأبجدية
# alphabet = string.ascii_lowercase

# # طلب إدخال الكلمة من المستخدم
# word = input("Please type a word: ").lower()

# # طلب إدخال عدد المسافات من المستخدم
# shift = int(input("Please enter the number of shifts: "))

# # تهيئة المتغير لتخزين الكلمة المشفرة
# encrypted_word = ""

# # تكرار على كل حرف في الكلمة المدخلة
# for letter in word:
#     if letter in alphabet:  # التحقق من أن الحرف جزء من الأبجدية
#         original_index = alphabet.index(letter)  # إيجاد فهرس الحرف الأصلي
#         new_position = (original_index + shift) % 26  # حساب الفهرس الجديد مع الالتفاف
#         encrypted_word += alphabet[new_position]  # إضافة الحرف المشفر للكلمة المشفرة
#     else:
#         encrypted_word += letter  # إضافة الحرف كما هو إذا لم يكن جزءًا من الأبجدية (مثل المسافات)

# # طباعة الكلمة المشفرة
# print(f"Here is the encrypted word: {encrypted_word}")
# تعريف الأبجدية
alphabet_lower = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

# طلب إدخال الرسالة من المستخدم
message = input("Enter a message: ")
shift = int(input("Please enter the number of shifts: "))

def encrypt(messages, shifts):
    encrypted_message = ""
    for letter in messages:
        if letter in alphabet_lower:  # التحقق إذا كان الحرف صغير
            original_index = alphabet_lower.index(letter)
            new_position = (original_index - shifts) % 26
            encrypted_message += alphabet_lower[new_position]
        elif letter in alphabet_upper:  # التحقق إذا كان الحرف كبير
            original_index = alphabet_upper.index(letter)
            new_position = (original_index + shifts) % 26
            encrypted_message += alphabet_upper[new_position]
        else:
            encrypted_message += letter  # إضافة الحرف كما هو إذا لم يكن جزءًا من الأبجدية

    print(encrypted_message)

encrypt(message, shift)

            


