print("welcome to  place the rabbit")
filed =[ ['🚪' , '🚪', '🚪'], ['🚪' , '🚪', '🚪'], ['🚪' , '🚪', '🚪']]

print ( f"{filed[0]} \n{filed[1]} \n{filed[2]} ")
print('\nwhere should the boy go? 🤷‍♂️')
position= (input("please choose a row and a column "))
row = int(position[0])
column = int(position[1])
filed[row-1][column-1]= '🤷‍♂️'
print('\n success.....\n')

print ( f"{filed[0]} \n{filed[1]} \n{filed[2]} ")
