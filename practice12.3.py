
with open('en-ru.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

ru_en = {}
for line in lines:
    if ' - ' not in line:
        continue
    en, ru = line.strip().split(' - ')
    for word in ru.split(', '):
        if word not in ru_en:
            ru_en[word] = []
        ru_en[word].append(en)

with open('ru-en.txt', 'w', encoding='utf-8') as f:
    for word in sorted(ru_en.keys()):
        f.write(f"{word} - {', '.join(ru_en[word])}\n")