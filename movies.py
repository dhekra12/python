# rate= 74
# viwes = 5400
# print(rate > 70 and viwes > 5000 )
# heart_art = [
#     "  ****   ****  ",
#     "***************",
#     "*****************",
#     "*****************",
#     " *****************",
#     "  *****************",
#     "   *****************",
#     "     *************",
#     "       *********",
#     "         *****",
#     "           *"
# ]

# print("\n".join(heart_art))
# print("\n      I Love You!")
def heart():
    for i in range(6):
        for j in range(7):
            if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 == 0) or (i - j == 2) or (i + j == 8):
                print("*", end="")
            elif i == 3 and j == 3:
                print("I love you", end="")
            else:
                print(" ", end="")
        print()

if __name__ == "__main__":
    heart()
