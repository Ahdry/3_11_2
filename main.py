def single_root_words(root_word, *other_words):
    # Приведем корневое слово к нижнему регистру для сравнения
    root_word_lower = root_word.lower()
    same_words = []  # Создаем пустой список для подходящих слов

    # Перебираем все слова в other_words
    for word in other_words:
        # Приведем текущее слово к нижнему регистру
        word_lower = word.lower()
        # Проверяем условия для добавления слова в список
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)  # Добавляем слово в список

    return same_words  # Возвращаем список подходящих слов


# Примеры вызова функции
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результата
print(result1)  # ['richiest', 'orichalcum', 'richies']
print(result2)  # ['Able', 'Disable']
