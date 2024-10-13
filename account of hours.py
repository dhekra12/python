input_seconds=int(input('please type the total second: \n'))
hours= input_seconds // 3600 
# remaining_seconds = input_seconds % 3600
minutes= (input_seconds% 3600) // 60
seconds= input_seconds % 60
print("Minutes:", minutes)
print("Hours:", hours)
print("Seconds:", seconds)