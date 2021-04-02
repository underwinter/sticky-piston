def basic():
    print("sticky piston v0.1(alpha-test) ")
    name = input("enter your name(required): ")
    print("Hi, " + name + "!")

    age = input("enter your age(required): ")
    print("You are already "+ age + " years old,cool!")

    password = input("Enter a difficult password (required): ")

    nickname = input("Enter a nickname (optional): ")
    print("Good nickname," + name )

    twofact = input("Enter any 2FA code: ")

    phone = input("Enter your phone number(required): ")
    print("your phone number is " + phone + ",yes?")

    bio = input("Enter your bio")

    print("new post")
    newpost = input("+: ")

    if newpost  == "+":
	    posttext = input("example: im love cats ")
	    print(posttext)
    else: print("error")

    print("one more thing?")
    secondpost = input("+")

    if secondpost == "+":
	    secondposttext = input("example: apple = banana ")
    else: print("im tired")

    print("Maybe third post?")
    thirdpost = input("+")

    if thirdpost == "+":
        thirdposttext = input("example: im pizza")
    else: print("ok")

    print("im a fourth post,do you want to see me?")
    fourthpost = input("+")

    if thirdpost == "+":
        fourthposttext = input("example: dogecoin is the best!")
    else: print("you and i you and i we with you are friends")
basic()

