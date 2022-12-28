import os
list_ = []
list_name = os.listdir('sorted')
for i in list_name:
    with open(f'sorted/{i}', encoding='utf-8') as f:
        lines = f.readlines()
        lines = [i + '\n'] + [str(len(lines)) + '\n'] + lines
        list_.append(lines)

text = '\n'.join(sum((sorted(list_, key=len)), []))

with open('all.txt', 'w', encoding='utf-8') as m:
    m.write(text)