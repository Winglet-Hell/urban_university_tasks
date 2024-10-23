def custom_write(file_name, strings):
    strings_positions = {}
    f = open(file_name, "w", encoding="utf-8")
    line_number = 1
    for line in strings:
        position = f.tell()
        f.write(line + "\n")
        strings_positions[(line_number, position)] = line
        line_number += 1
    f.close()
    return strings_positions


info = [
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!",
]

result = custom_write("test.txt", info)
for elem in result.items():
    print(elem)
