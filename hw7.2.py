def correct_sentence(text):
    text = text.capitalize()  # Перша літера має бути великою
    if not text.endswith('.'):  # Додаємо крапку, якщо її немає
        text += '.'
    return text

# Перевірка тестами
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')