word = input()

vowels_letters = {'a', 'e', 'i', 'o', 'u'}

vowels_count = 0
consonants_count = 0

for letter in word:
    if letter in vowels_letters:
        vowels_count += 1
    else:
        consonants_count += 1

print(f"Гласных: {vowels_count}, Согласных: {consonants_count}")

for v in ['a', 'e', 'i', 'o', 'u']:
    count = word.count(v)
    if count > 0:
        print(f"Буква '{v}': {count}")
    else:
        print(f"Буква '{v}': False")
