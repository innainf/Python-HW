def format_time(seconds):
    # Обчислюємо кількість днів
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, secs = divmod(remainder, 60)

    # Визначаємо правильне слово для "день"
    if days == 1:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"

    # Форматуємо години, хвилини, секунди з провідними нулями
    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}"

    return f"{days} {day_word}, {time_str}"


# Ввід користувача
user_input = int(input("Введіть кількість секунд (0 до 8640000): "))
if 0 <= user_input < 8640000:
    print(format_time(user_input))
else:
    print("Число повинно бути від 0 до 8640000.")