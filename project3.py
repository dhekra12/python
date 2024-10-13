print("""
  ☠️ ☠️ ☠️ ☠️ ☠️
      """)
print('welcome to my island')
print("there are two doors in front of you. 🚪 a red door and 🚪 a blue door")
door = input("Which door do you want ").lower()
# check user's choice
if door== "red":
    print ("Great! now you entered a room.\n you found three boxes: 🎁 white , 🎁 black , 🎁 green")
    boxes= input("Which box do you open? ").lower()
    if boxes == "white":
     print("Oops! you opened a box filled with snakes 🐍🐍🐍")
    elif boxes == "black":
      print("Oops! you opened a box filed with spiders 🕷️🕷️🕷️")
    elif boxes == "green":
     print ("congratulations! you found the treasure! 💰💰💰")
    else:
     print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")

elif door == "blue":
 print("Oops! you found the crocodile door.\n Game over 🐊🐊🐊 ") 
else :
    print("Invalid choice! 🤷‍♂️🤷‍♂️🤷‍♂️")
 