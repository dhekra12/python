import string
 
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.punctuation)
sentence = input("Please type a sentence: ")
new_sentence= ""
for x in sentence:
    if x not in string.punctuation:
        new_sentence += x
        print("\n\n*** Here is the same sentence without punctuation *** \n\n" , new_sentence)

    
    