# x= 5
# x+=10
# print(x)
# y  = 'hello '
# y+= 'world\n'
# y*=3
# print(y)

numbers = [1, 2, 3, 4, 5]
total = 0
print("Let's add each number to the next ")

for i in numbers:
    total +=i
    print(f"-> {total} ")   
    print(f"the total number is: {total}")
    # shift + tab for back space