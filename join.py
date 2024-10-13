# names =['taha', 'dhekra', 'yusra', 'ahmed', 'ali', 'mohammed' , 'paradise']
# print((names[1:7:2]))
# # separator = '\n'
# print( '🤷‍♂️ '.join(names))

names_of_friends=input("Enter the first and last name of your friends separated by comma: ").split(', ')
abbreviated_name = []

   
for name in names_of_friends:
    name_parts= name.split()
    print(name_parts)
    # name.capitalize()
    first_name = name_parts[0]
    last_name = name_parts[1]
    first_initial = first_name[0]
    last_initial =last_name[0]
    abbreviation = first_initial + '.' + last_initial + '.'
    abbreviated_name.append(abbreviation)
    
    
print("Abbreviated Names: ")
for x in abbreviated_name:
    print(x)