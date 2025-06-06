import string

def letters_between(dash_input):
    # Отримуємо всі букви з string.ascii_letters
    letters = string.ascii_letters

    # Розділяємо рядок за дефісом
    start, end = dash_input.split('-')

    # Знаходимо індекси початкової та кінцевої літери
    start_index = letters.index(start)
    end_index = letters.index(end)

    # Повертаємо підрядок між ними (включно)
    return letters[start_index:end_index + 1]

# Приклади використання:
print(letters_between("a-c"))   # abc
print(letters_between("a-a"))   # a
print(letters_between("s-H"))   # stuvwxyzABCDEFGH
print(letters_between("a-A"))   # abcdefghijklmnopqrstuvwxyzA