def analyze_string():
    text = input("Введите строку: ").strip()
    
    if not text:
        print("Строка пустая!")
        return
    
    words = text.split()
    
    even_length_count = 0
    longest_word = ""

    for word in words:
        if len(word) % 2 == 0:
            even_length_count += 1
        if len(word) > len(longest_word):
            longest_word = word
    
    print(f"\nРезультаты анализа строки:")
    print(f"Количество слов с четной длиной: {even_length_count}")
    print(f"Самое длинное слово: '{longest_word}' (длина: {len(longest_word)})")