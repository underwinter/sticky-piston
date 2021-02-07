print("липкий поршень 0.01 (PRE-DEVELOPER-ALPHA)")
name = input("Введи своё имя(обязательно): ")
print("Привет " + name )

age = input("Введи свой возраст(обязательно): ")
print("Тебе " + age + " лет(года),круто!")

email = input("Напиши адрес своей электронной почты для восстановления пароля(необязатяльно): ")
print("твоя почта " + email )

password = input("Введи трудный пароль(обязательно), самые лёгкие пароли тут:https://www.ph4.ru/pass_passlist.php: ")

nickname = input("Введи никнейм,если хочешь: ")
print("Хороший ник," + name )

print("новый пост")
newpost = input("+: ")

if newpost  == "+":
	posttext = input("пример: вчера я ходил на самбо")
else: print("не понял")

input()