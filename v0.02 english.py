print("sticky piston 0.02 (developer alpha) ")
name = input("enter your name(required): ")
print("Hi, " + name + "!")

age = input("enter your age(required): ")
print("You are already "+ age + " years old,cool!")

email = input("Enter your email address (optional): ")
print("your email is " + email + ",yes?")

password = input("Enter a difficult password (required): ")

nickname = input("Enter a nickname (optional): ")
print("Good nickname," + name )

twofact = input("Enter any 2FA code: ")

phone = input("Enter your phone number(required): ")
print("your phone number is " + email + ",yes?")

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
else: input()