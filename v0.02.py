print("sticky piston 0.02 (developer alpha) ")
name = input("Введи своё имя(обяз): ")
print("Привет " + name )

age = input("Введи свой возраст(обяз): ")
print("Тебе " + age + " лет(года),круто!")

email = input("Напиши адрес своей электронной почты для восстановления пароля(необязатяльно): ")
print("твоя почта " + email )

password = input("Введи трудный пароль(обяз), самые лёгкие пароли тут:https://www.ph4.ru/pass_passlist.php: ")

nickname = input("Введи никнейм,если хочешь: ")
print("Хороший ник," + name )

twofact = input("введи код с любого генератора кодов(необяз): ")

phone = input("Введи свой номер телефона(обяз): ")
print("твой номер телефона " + phone )

print("новый пост")
newpost = input("+: ")

if newpost  == "+":
	posttext = input("пример: вчера я ходил на самбо ")
	print(posttext)
else: print("не понял")

print("ещё один пост?")
secondpost = input("+")

if secondpost == "+":
	secondposttext = input("пример: вчера я ходил на скрэтч ")
else: input()