vowels = 'аяуюоеёэиыaeiou'
while True:
    word = input('Слово: ').lower()
    if word == 'break':
        print('Программа завершена!')
        break
    print(f'Количество букв: {len(word)}')
    vowels_count = consonant_count = 0
    for i in word:
        if i in vowels:
            vowels_count += 1
        elif i.isalpha():
            consonant_count += 1
    print(f'Согласных букв: {consonant_count}\nГласных букв: {vowels_count}')
    vowels_ratio = round(vowels_count * 100 / len(word), 2)
    consonant_ratio = round(consonant_count * 100 / len(word), 2)
    print(f'Гласные/Согласные: {vowels_ratio}% / {consonant_ratio}%')
