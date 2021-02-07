i = 1000
while i < 100:
    print (i)
    i += 2

for j in 'hello world':
    if j == 'w':
        break
    print(j * 2, end = '')

print("sticky piston 0.03 (pre-alpha) ")
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
else: print("wait 0.04 version")