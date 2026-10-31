name = input("Введіть ваше ім'я: ")
age = input("Введіть ваш вік: ")

print(f"Привіт {name}, тобі {age}!")


age = int(input("Введіть ваш вік: "))

if age >= 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")



import random

    secret_number = random.randint(1, 10)
    attempts = 3

    print("Я загадав число від 1 до 10. У тебе є 3 спроби!")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Спроба #{attempt}. Введіть число: "))

        if guess == secret_number:
            print("Вітаю! Ти вгадав число!")
            break
        elif guess > secret_number:
            print("Менше")
        else:
            print("Більше")
    else:
        print(f"Спроби закінчилися! Я загадав число: {secret_number}")


start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

# range(start, end + 1) включає останнє число
for number in range(start, end + 1):
    print(number)


n = int(input("Введіть число n: "))

for number in range(n, 0, -1):
    if number % 2 == 0:
        print(number, end=" ")
        continue

score = int(input("Введіть кількість балів за екзамен (0-100): "))

if score >= 90:
    print("Ваша оцінка: Відмінно (A)")
elif score >= 75:
    print("Ваша оцінка: Добре (B / C)")
elif score >= 60:
    print("Ваша оцінка: Задовільно (D / E)")
else:
    print("Ваша оцінка: Незадовільно (F), потрібно перездати.")
