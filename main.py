# input number
num = int(input("Enter number: "))

# check if number is greater than 3 and odd
if (num <= 3):
    print("Number should be greater than 3")
elif (num % 2) == 0:
    print("Odd number only")
else:
    # draw rhombus accending
    star = "{}".format("*"*(num-(num-1)))
    for i in range(1,(num+1)//2):
        drawing = star.center(num)
        print(drawing)
        star += "**"

    # draw rhombus decending
    star = "{}".format("*"*num)
    for i in range((num+1)//2, 0, -1):
        drawing = star.center(num)
        print(drawing)
        splitStars = list(star)
        removeStars = splitStars[:-2]
        star = "".join(removeStars)

