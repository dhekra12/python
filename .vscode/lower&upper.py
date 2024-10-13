# area=input('chose an area: (Dhamar),  (Sanaa) , or (Taiz)')
# if area.lower() == "dhamar" or area.upper() == "SANAA" or area.lower()== "taiz" : 
#   print(f' {area} is on our list')

# else:
#      print(f'sorry, {area} is not on our list')

# name=input('please enter your name\n')
# passward=input('please enter your passward')
# if name.lower()=='yousre'and passward=='1234':
#      print('hello')
# else :
#     print('sorry,is not on our list') 
age= int(input('Enter your age \n'))
License= input('Do you have License type (Yes) or (No)')
if age >= 18  and License.lower() == 'yes':
        print('You can drive!')
elif age < 18 or License.lower() == 'no':
        print('you can not drive')
else:
    print(f'your entery of [{License}] is not understood')